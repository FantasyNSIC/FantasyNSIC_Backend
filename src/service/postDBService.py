"""Service POST functions for posting/retrieving data to the database"""

from ..util.connection import connect_to_fantasyDB
from .classes.NSIC_Player import NSIC_Player
from .classes.NSIC_Team import NSIC_Team
from .classes.Player_Stats_2023 import Player_Stats_2023
from .classes.Player_Stats_Week import Player_Stats_Week
from .classes.responses.NSICPlayerResponse import NSICPlayerResponse

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
