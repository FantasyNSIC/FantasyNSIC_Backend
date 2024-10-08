"""Service POST functions for posting/retrieving data to the database"""

from ..util.connection import connect_to_fantasyDB
from .classes.NSIC_Player import NSIC_Player
from .classes.NSIC_Team import NSIC_Team
from .classes.Player_Stats_2023 import Player_Stats_2023
from .classes.Player_Stats_Week import Player_Stats_Week
from .classes.responses.NSICPlayerResponse import NSICPlayerResponse
from .classes.responses.ConfirmationResponse import ConfirmationResponse
from ..service.service_handlers.addPlayerToRosterHandle import handle_new_player_to_roster_determination
from ..service.service_handlers.matchupRosterHandle import matchup_roster_creation

def get_nsic_player_service(player_id):
    """
    Fetches information about a NSIC player from the database.
    :param player_id: The ID of the player.
    """
    # Initialize empty response object.
    player_info = None
    player_stats_2023 = None
    weekly_stats = []
    nsic_player_info = NSICPlayerResponse(NSIC_Player.empty_player(),
                                          NSIC_Team.empty_team(),
                                          Player_Stats_2023.empty_stats(0), [])
    conn = connect_to_fantasyDB()
    cur = conn.cursor()

    # Execute queries to get player information.
    try:
        # Get player and team information.
        with open('src/queries/get_nsic_player_information.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (player_id,))
        player_info = cur.fetchone()

        # Get player 2023 statistics.
        with open('src/queries/get_nsic_player_stats_2023.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (player_id,))
        res_player_stats_2023 = cur.fetchone()
        if res_player_stats_2023 is not None:
            player_stats_2023 = Player_Stats_2023.from_tuple(res_player_stats_2023)
        else:
            player_stats_2023 = Player_Stats_2023.empty_stats(player_id)

        # Get player weekly statistics.
        with open('src/queries/get_nsic_player_stats_weekly.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (player_id,))
        res_weekly_stats = cur.fetchone()
        res_weekly_stats = [res_weekly_stats[i:i + 17] for i in range(0, len(res_weekly_stats), 17)]
        for stats in res_weekly_stats:
            weekly_stats.append(Player_Stats_Week.from_tuple(stats))

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    if player_info is not None:
        nsic_player_info = NSICPlayerResponse(NSIC_Player.from_tuple(player_info[0:10]),
                                              NSIC_Team.from_tuple(player_info[10:]),
                                              player_stats_2023,
                                              weekly_stats)
        return nsic_player_info
    return nsic_player_info

def get_user_team_roster_service(league_id, user_team_id):
    """
    Fetches a user's team roster from the database.
    :param league_id: The ID of the league.
    :param user_team_id: The ID of the user's team.
    """
    # Initialize empty response objects.
    conn = connect_to_fantasyDB()
    cur = conn.cursor()
    formatted_roster = None

    # Execute queries to get user team roster information.
    try:
        # Get league constraints.
        with open('src/queries/get_league_information.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (league_id,))
        league_info_res = cur.fetchone()
        constraints = league_info_res[1]

        # Get user team roster.
        with open('src/queries/get_user_team_roster.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (user_team_id,))
        res_roster = cur.fetchall()
        formatted_roster = matchup_roster_creation(res_roster, int(user_team_id), constraints)

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    return formatted_roster

def get_nsic_player_weekly_stats_service(player_id, week):
    """
    Fetches weekly statistics for a NSIC player from the database.
    :param player_id: The ID of the player.
    :param week: The week number.
    """
    # Initialize empty response object.
    weekly_stats = Player_Stats_Week.empty()
    conn = connect_to_fantasyDB()
    cur = conn.cursor()
    week = "week_" + str(week)

    # Execute queries to get player weekly statistics.
    try:
        with open('src/queries/get_nsic_single_week_stats.sql', 'r') as sql:
            query_temp = sql.read()
        query = query_temp.format(week=week)
        cur.execute(query, (player_id,))
        res_weekly_stats = cur.fetchone()
        if res_weekly_stats is not None:
            weekly_stats = Player_Stats_Week.from_tuple(res_weekly_stats)

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    if weekly_stats is not None:
        return weekly_stats
    return weekly_stats

def add_nsic_player_to_roster_service(player_id, user_team_id, league_id):
    """
    Adds a NSIC player to a user's roster.
    :param player_id: The ID of the player.
    :param user_team_id: The ID of the user's team.
    :param league_id: The ID of the league.
    """
    # Initialize empty response object and connection.
    conn = connect_to_fantasyDB()
    cur = conn.cursor()
    response = ConfirmationResponse(False, "Failed to add player to roster.")

    # Execute queries to determine if player can be added to roster.
    # if they can, add them to the roster. Otherwise, return a failure response.
    try:
        # CASE 1: Does NSIC player_id exist?
        with open('src/queries/check_nsic_player_exists.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (player_id,))
        player_res = cur.fetchone()
        if player_res is None:
            response.message = "Failed to add player to roster. NSIC Player does not exist."
            return response
        player_pos = player_res[4]
        
        # CASE 2: Is the NSIC player already taken?
        with open('src/queries/check_if_nsic_player_is_taken.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (league_id, player_id))
        if cur.fetchone() is not None:
            response.message = "Failed to add player to roster. NSIC Player is already taken."
            return response
        
        # CASE 3: Is the user's roster full?
        # Fetch league constraints.
        with open('src/queries/get_league_information.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (league_id,))
        league_info_res = cur.fetchone()
        constraints = league_info_res[1]
        # Check if roster is full.
        with open('src/queries/get_my_team_roster_players.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (user_team_id,))
        res_roster = cur.fetchall()
        roster_spot = handle_new_player_to_roster_determination(res_roster, constraints, player_pos)
        if not roster_spot[0]:
            response.message = "Failed to add player to roster. Your roster is full, Please drop a player first."
            return response
        
        # If all cases pass, add player to roster.
        with open('src/queries/insert_into_taken_players.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (league_id, user_team_id, player_id))
        with open('src/queries/insert_into_team_roster.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (user_team_id, player_id, roster_spot[1], player_pos))
        conn.commit()
        response.success = True
        response.message = "Player added to roster successfully."
        
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    return response

def drop_nsic_player_from_roster_service(player_id, user_team_id, league_id):
    """
    Drops a NSIC player from a user's roster.
    :param player_id: The ID of the player.
    :param user_team_id: The ID of the user's team.
    :param league_id: The ID of the league.
    """
    # Initialize empty response object and connection.
    conn = connect_to_fantasyDB()
    cur = conn.cursor()
    response = ConfirmationResponse(False, "Failed to drop player from roster.")

    # Execute queries to determine if player can be dropped from roster.
    # if they can, drop them from the roster. Otherwise, return a failure response.
    try:
        # CASE 1: Is the NSIC player on the user's roster?
        with open('src/queries/check_nsic_player_on_roster.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (user_team_id, player_id, league_id))
        if cur.fetchone() is None:
            response.message = "Failed to drop player from roster. NSIC Player is not on your roster."
            return response
        
        # If all cases pass, drop player from roster.
        with open('src/queries/delete_from_taken_players.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (league_id, user_team_id, player_id))
        with open('src/queries/delete_from_team_roster.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (user_team_id, player_id))
        conn.commit()
        response.success = True
        response.message = "Player dropped from roster successfully."
        
    except Exception as e:
        print(e)
        response.message = str(e)
        return response
    finally:
        cur.close()
        conn.close()
    return response

def move_nsic_players_on_roster_service(user_team_id, league_id, player_id_1, player_id_2):
    """
    Moves NSIC players on a user's roster.
    :param user_team_id: The ID of the user's team.
    :param player_1: The ID of the first player.
    :param player_2: The ID of the second player, can be Null.
    """
    # Initialize empty response object and connection.
    conn = connect_to_fantasyDB()
    cur = conn.cursor()
    response = ConfirmationResponse(False, "Failed to move players on roster.")

    # Execute queries to determine if players can be moved on roster.
    # if they can, move them on the roster. Otherwise, return a failure response.
    try:
        # CASE 1: Are the NSIC players on the user's roster?
        # Player 1
        if player_id_1 is None:
            response.message = "Failed to move players on roster. NSIC Player 1 cannot be null."
            return response
        if player_id_1 == player_id_2:
            response.message = "Failed to move players on roster. NSIC Player 1 and 2 cannot be the same."
            return response
        with open('src/queries/check_nsic_player_on_roster.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (user_team_id, player_id_1, league_id))
        player_1_res = cur.fetchone()
        if player_1_res is None:
            response.message = "Failed to move players on roster. NSIC Player 1 is not on your roster."
            return response
        player_1_status = player_1_res[2]
        player_2_status = None
        # Player 2
        if player_id_2 is not None:
            cur.execute(query, (user_team_id, player_id_2, league_id))
            player_2_res = cur.fetchone()
            if player_2_res is None:
                response.message = "Failed to move players on roster. NSIC Player 2 is not on your roster."
                return response
            player_2_status = player_2_res[2]
        
        # If all cases pass, move players on roster. If player 2's status exists, swap them.
        # If player 2's status is None, move player 1 to the opposite status.
        if player_2_status is not None:
            with open('src/queries/move_NSIC_player_swap_status.sql', 'r') as sql:
                query = sql.read()
            cur.execute(query, (player_2_status, player_id_1, user_team_id,
                                player_1_status, player_id_2, user_team_id))
        elif player_2_status is None and player_1_status == 'active':
            with open('src/queries/move_NSIC_player_to_bench.sql', 'r') as sql:
                query = sql.read()
            cur.execute(query, (player_id_1, user_team_id))
        elif player_2_status is None and player_1_status == 'bench':
            with open('src/queries/move_NSIC_player_to_active.sql', 'r') as sql:
                query = sql.read()
            cur.execute(query, (player_id_1, user_team_id))
        else:
            response.message = "Failed to move players on roster. Invalid move."
            return response
        conn.commit()
        response.success = True
        response.message = "Players moved on roster successfully."
        
    except Exception as e:
        print(e)
        response.message = str(e)
        return response
    finally:
        cur.close()
        conn.close()
    return response

def draft_nsic_player_to_roster_service(player_id, draft_pick, user_team_id, league_id):
    """
    Drafts a NSIC player to a user's roster.
    :param player_id: The ID of the player.
    :param user_team_id: The ID of the user's team.
    :param league_id: The ID of the league.
    """
    # Initialize empty response object.
    response_draft = ConfirmationResponse(False, "Failed to draft player to roster.")
    conn = connect_to_fantasyDB()
    cur = conn.cursor()

    try:
        # First, check to see if draft pick is valid.
        with open('src/queries/check_draft_pick_is_valid.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (draft_pick, league_id, user_team_id))
        pick = cur.fetchone()
        if pick is None:
            response_draft.message = "Failed to draft player to roster. Invalid draft pick."
            return response_draft
        elif pick[3] is not None:
            response_draft.message = "Failed to draft player to roster. Draft pick has already been used."
            return response_draft
        
        # Then, attempt to add drafted player to roster.
        response_add = add_nsic_player_to_roster_service(player_id, user_team_id, league_id)

        # If the player was successfully added to the roster, add drafted player to draft pick.
        if response_add.success:
            with open('src/queries/update_draft_order_pick.sql', 'r') as sql:
                query = sql.read()
            cur.execute(query, (player_id, draft_pick, league_id, user_team_id))
            conn.commit()
            response_draft.success = True
            response_draft.message = "Player drafted to roster successfully."
        else:
            response_draft.message = response_add.message
    except Exception as e:
        print(e)
        response_draft.message = str(e)
    finally:
        cur.close()
        conn.close()
    return response_draft

def submit_waiver_wire_claim_service(user_team_id, league_id, player_add, player_remove = None):
    """
    Submits a waiver wire claim.
    :param user_team_id: The ID of the user's team.
    :param league_id: The ID of the league.
    :param player_add: The ID of the player to add.
    :param player_remove: The ID of the player to remove.
    """
    # Initialize empty response object and connection.
    conn = connect_to_fantasyDB()
    cur = conn.cursor()
    response = ConfirmationResponse(False, "Failed to submit waiver wire claim.")

    # Execute queries to determine if waiver wire claim can be submitted.
    # if they can, submit the claim. Otherwise, return a failure response.
    try:
        # CASE 1: Does NSIC player_id exist?
        if player_add is None:
            response.message = "Failed to submit waiver claim. Added player cannot be null."
            return response
        if player_add == player_remove:
            response.message = "Failed to submit waiver claim, Added and Removed player cannot be the same."
            return response
        with open('src/queries/check_nsic_player_exists.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (player_add,))
        player_res = cur.fetchone()
        if player_res is None:
            response.message = "Failed to submit waiver claim. Added player does not exist."
            return response
        
        # CASE 2: is the added player already taken?
        with open('src/queries/check_if_nsic_player_is_taken.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (league_id, player_add))
        player_add_res = cur.fetchone()
        if player_add_res is not None:
            response.message = "Failed to submit waiver claim. Added player is not available."
            return response
        
        # CASE 3: is the removed player on the user's roster?
        if player_remove is not None:
            with open('src/queries/check_nsic_player_on_roster.sql', 'r') as sql:
                query = sql.read()
            cur.execute(query, (user_team_id, player_remove, league_id))
            player_remove_res = cur.fetchone()
            if player_remove_res is None:
                response.message = "Failed to submit waiver claim. Removed player is not on your roster."
                return response
        
        # If all cases pass, submit waiver wire claim.
        with open('src/queries/waiver_wire_submit_claim.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (league_id, user_team_id, player_add, player_remove))
        conn.commit()
        response.success = True
        response.message = "Waiver wire claim submitted successfully."
        
    except Exception as e:
        print(e)
        response.message = str(e)
        return response
    finally:
        cur.close()
        conn.close()
    return response

def delete_waiver_wire_claim_service(user_team_id, league_id, player_add, player_remove = None):
    """
    Deletes a waiver wire claim.
    :param user_team_id: The ID of the user's team.
    :param league_id: The ID of the league.
    :param player_add: The ID of the player to add.
    :param player_remove: The ID of the player to remove.
    """
    # Initialize empty response object and connection.
    conn = connect_to_fantasyDB()
    cur = conn.cursor()
    response = ConfirmationResponse(False, "Failed to delete waiver wire claim.")

    # Execute queries to determine if waiver wire claim can be deleted.
    # if they can, delete the claim. Otherwise, return a failure response.
    try:
        # CASE 1: Is the waiver wire claim valid?
        if player_remove is not None:
            with open('src/queries/waiver_wire_check_valid_claim.sql', 'r') as sql:
                query = sql.read()
            cur.execute(query, (league_id, user_team_id, player_add, player_remove))
        else:
            with open('src/queries/waiver_wire_check_valid_null.sql', 'r') as sql:
                query = sql.read()
            cur.execute(query, (league_id, user_team_id, player_add))
        if cur.fetchone() is None:
            response.message = "Failed to delete waiver wire claim. Invalid waiver wire claim."
            return response
        
        # If all cases pass, delete waiver wire claim.
        if player_remove is not None:
            with open('src/queries/waiver_wire_delete_claim.sql', 'r') as sql:
                query = sql.read()
            cur.execute(query, (league_id, user_team_id, player_add, player_remove))
        else:
            with open('src/queries/waiver_wire_delete_claim_null.sql', 'r') as sql:
                query = sql.read()
            cur.execute(query, (league_id, user_team_id, player_add))
        conn.commit()
        response.success = True
        response.message = "Waiver wire claim deleted successfully."

    except Exception as e:
        print(e)
        response.message = str(e)
        return response
    finally:
        cur.close()
        conn.close()
    return response
