"""Service GET functions for getting data from the database"""

from ..util.connection import connect_to_fantasyDB
from .classes.NSIC_Player import NSIC_Player
from .classes.User_Roster import UserRoster
from .classes.responses.MyTeamInfoResponse import MyTeamInfoResponse
from .classes.responses.AvailablePlayersResponse import AvailablePlayersResponse

def my_team_information_service(user_team_id, league_id):
    """
    Fetches information about the user's team from the database.
    :param user_team_id: The ID of the user's team.
    :param league_id: The ID of the user's league.
    """
    # Initialize empty response object.
    my_team_info = MyTeamInfoResponse('', '', '', '', 0, 0, None)
    conn = connect_to_fantasyDB()
    cur = conn.cursor()

    # Execute queries to get team information.
    try:
        # Get team name.
        query = 'SELECT team_name FROM user_team WHERE user_team_id = %s'
        cur.execute(query, (user_team_id,))
        team_name = cur.fetchone()

        # Get league name and constarint.
        query = 'SELECT league_name, league_constraint FROM leagues WHERE league_id = %s'
        cur.execute(query, (league_id,))
        league_info = cur.fetchone()

        # Get user full name.
        with open('src/queries/get_my_team_full_name.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (user_team_id,))
        user_full_name = cur.fetchone()

        # Get team wins and losses.
        query = 'SELECT wins, losses FROM team_records WHERE user_team_id = %s'
        cur.execute(query, (user_team_id,))
        team_record = cur.fetchone()

        # Get team's roster, form roster object.
        roster = UserRoster()
        with open('src/queries/get_my_team_roster_players.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (user_team_id,))
        res_roster = cur.fetchall()
        for player in res_roster:
            new_player = NSIC_Player.from_tuple(player[1:])
            roster.add_player(new_player, player[0])

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    my_team_info = MyTeamInfoResponse(
        team_name[0], league_info[0], league_info[1], user_full_name[0], team_record[0], team_record[1], roster)
    return my_team_info

def available_players_service(league_id):
    """
    Fetches available players from the database.
    :param league_id: The ID of the user's league.
    """
    # Read SQL query from file, connect to DB.
    available_players = []
    with open('src/queries/get_available_players.sql', 'r') as sql:
        query = sql.read()
    conn = connect_to_fantasyDB()
    cur = conn.cursor()

    # Execute query to get available players.
    try:
        cur.execute(query, (league_id,))
        fetched_players = cur.fetchall()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    available_players = AvailablePlayersResponse.from_tuple(fetched_players)
    return available_players
