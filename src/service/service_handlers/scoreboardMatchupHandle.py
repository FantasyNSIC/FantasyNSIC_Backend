"""Hanlde functions for formating matchups and building Weekly_Matchup classes"""
from ..classes.Week_Matchup import Week_Matchup
from ..classes.User_Team import User_Team

def format_weekly_matchups(scoreboard_tuples):
    """
    Takes in a response list of tuples and returns Weekly_Matchups classes.
    """
    matchups = []
    for user_team in scoreboard_tuples:
        # Create Team 1 from info
        user_info_1 = user_team[2:]
        team_1 = User_Team.from_tuple(user_info_1[0:4])

        # Filter out Team 2 from results using user_team_id
        user_info_2 = next((users for users in scoreboard_tuples if users[1] == team_1.user_team_id), None)

        # Create Team 2 from info
        if user_info_2 is not None:
            user_info_2 = user_info_2[2:]
        else:
            user_info_2 = 0, 0, "", 0, 0.00, 0, 0
        team_2 = User_Team.from_tuple(user_info_2[0:4])

        # Build matchup and store.
        matchup = Week_Matchup(team_1, team_2, float(user_info_1[4]), float(user_info_2[4]), user_info_1[5],
                               user_info_2[5], user_info_1[6], user_info_2[6])
        
         # filter out matchups that already exist
        if not any(matchup.team_1.user_team_id == match.team_2.user_team_id for match in matchups):
            matchups.append(matchup)

    return matchups
