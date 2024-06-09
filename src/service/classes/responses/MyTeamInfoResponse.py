import json
from ..User_Roster import UserRoster

class MyTeamInfoResponse:
    def __init__(self,
                 teamName: str,
                 leagueName: str,
                 leagueConstraint: str,
                 userName: str,
                 wins: int,
                 losses: int,
                 roster: UserRoster) -> None:
        
        self.teamName = teamName
        self.leagueName = leagueName
        self.leagueConstraint = leagueConstraint
        self.userName = userName
        self.wins = wins
        self.losses = losses
        self.roster = roster

    def get_teamName(self) -> str:
        """
        Get the team name.
        """
        return self.teamName

    def set_teamName(self, teamName: str) -> None:
        """
        Set the team name.
        """
        self.teamName = teamName

    def get_leagueName(self) -> str:
        """
        Get the league name.
        """
        return self.leagueName

    def set_leagueName(self, leagueName: str) -> None:
        """
        Set the league name.
        """
        self.leagueName = leagueName

    def get_leagueConstraint(self) -> str:
        """
        Get the league constraint.
        """
        return self.leagueConstraint

    def set_leagueConstraint(self, leagueConstraint: str) -> None:
        """
        Set the league constraint.
        """
        self.leagueConstraint = leagueConstraint

    def get_userName(self) -> str:
        """
        Get the user name.
        """
        return self.userName

    def set_userName(self, userName: str) -> None:
        """
        Set the user name.
        """
        self.userName = userName

    def get_wins(self) -> int:
        """
        Get the number of wins.
        """
        return self.wins

    def set_wins(self, wins: int) -> None:
        """
        Set the number of wins.
        """
        self.wins = wins

    def get_losses(self) -> int:
        """
        Get the number of losses.
        """
        return self.losses

    def set_losses(self, losses: int) -> None:
        """
        Set the number of losses.
        """
        self.losses = losses

    def get_roster(self) -> UserRoster:
        """
        Get the user roster.
        """
        return self.roster

    def set_roster(self, roster: UserRoster) -> None:
        """
        Set the user roster.
        """
        self.roster = roster
        
    def toJson(self) -> str:
        """
        Convert the object to a JSON string.
        """
        return json.dumps(self.__dict__, default=lambda o: o.toJson() if hasattr(o, 'toJson') else str(o))
