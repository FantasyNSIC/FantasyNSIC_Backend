"""Service GET functions for getting data from the database"""

from ..util.connection import connect_to_fantasyDB
from .classes.NSIC_Player import NSIC_Player
from .classes.User_Roster import UserRoster
from .classes.responses.MyTeamInfoResponse import MyTeamInfoResponse
from .classes.responses.AvailablePlayersResponse import AvailablePlayersResponse
from .classes.responses.LeagueInfoResponse import LeagueInfoResponse
from .classes.responses.StandingsInfoResponse import StandingsInfoResponse
from .service_handlers.myTeamRosterHandle import handle_roster_creation

def my_team_information_service(user_team_id):
    """
    Fetches information about the user's team from the database.
    :param user_team_id: The ID of the user's team.
    :param league_id: The ID of the user's league.
    """
    # Initialize empty response object.
    my_team_info = MyTeamInfoResponse('', '', '', 0, 0, UserRoster())
    res_team_info = None
    formatted_roster = UserRoster()
    overflowFlag = False
    overflowPos = ""
    conn = connect_to_fantasyDB()
    cur = conn.cursor()

    # Execute queries to get team information.
    try:
        # Get team name, user's full name, league name, constraints, wins, and losses.
        with open('src/queries/get_my_team_information.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (user_team_id,))
        res_team_info = cur.fetchone()

        # Get team's roster, form roster object.
        roster = UserRoster()
        with open('src/queries/get_my_team_roster_players.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (user_team_id,))
        res_roster = cur.fetchall()
        handle_roster = handle_roster_creation(res_roster, res_team_info[0])
        formatted_roster = handle_roster[0]
        if handle_roster[1] != "":
            overflowFlag = True
            overflowPos = handle_roster[1]

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    if res_team_info is not None:
        my_team_info = MyTeamInfoResponse(
            res_team_info[1], res_team_info[2], res_team_info[3], res_team_info[4],
            res_team_info[5], formatted_roster, overflowFlag, overflowPos)
        return my_team_info
    return my_team_info

def available_players_service(league_id):
    """
    Fetches available players from the database.
    :param league_id: The ID of the user's league.
    """
    # Read SQL query from file, connect to DB.
    available_players = AvailablePlayersResponse([])
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

def league_information_service(league_id):
    """
    Fetches league information from the database.
    :param league_id: The ID of the user's league.
    """
    # Initialize empty response object.
    league_info = LeagueInfoResponse('', '', [])
    res_league_info = None
    res_league_tuples = []
    conn = connect_to_fantasyDB()
    cur = conn.cursor()

    # Execute queries to get league information.
    try:
        # Get league name and constraint.
        with open('src/queries/get_league_information.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (league_id,))
        res_league_info = cur.fetchone()
        res_league_tuples.append(res_league_info)

        # Get league teams, form league info response object.
        with open('src/queries/get_league_teams.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (league_id,))
        res_teams = cur.fetchall()
        res_league_tuples.append(res_teams)

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    if res_league_info is not None:
        league_info = LeagueInfoResponse.from_tuple(res_league_tuples)
        return league_info
    return league_info

def standings_information_service(league_id):
    """
    Fetches standings information from the database.
    :param league_id: The ID of the user's league.
    """
    # Read SQL query from file, connect to DB.
    standings = StandingsInfoResponse([])
    with open('src/queries/get_standings_information.sql', 'r') as sql:
        query = sql.read()
    conn = connect_to_fantasyDB()
    cur = conn.cursor()

    # Execute query to get standings.
    try:
        cur.execute(query, (league_id,))
        fetched_standings = cur.fetchall()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    print(fetched_standings)
    standings = StandingsInfoResponse.from_tuple(fetched_standings)
    return standings
