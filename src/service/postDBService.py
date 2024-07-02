"""Service POST functions for posting/retrieving data to the database"""

from ..util.connection import connect_to_fantasyDB
from .classes.NSIC_Player import NSIC_Player
from .classes.NSIC_Team import NSIC_Team
from .classes.Player_Stats_2023 import Player_Stats_2023
from .classes.Player_Stats_Week import Player_Stats_Week
from .classes.responses.NSICPlayerResponse import NSICPlayerResponse
from .classes.responses.ConfirmationResponse import ConfirmationResponse
from ..service.service_handlers.addPlayerToRosterHandle import handle_new_player_to_roster_determination

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
        # CASE 1: Does NSIC player_id exist?
        with open('src/queries/check_nsic_player_exists.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (player_id,))
        if cur.fetchone() is None:
            response.message = "Failed to drop player from roster. NSIC Player does not exist."
            return response

        # CASE 2: Is the NSIC player on the user's roster?
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
