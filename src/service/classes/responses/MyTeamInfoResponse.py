import json
from ..User_Roster import UserRoster

class MyTeamInfoResponse:
    def __init__(self,
                 teamName: str,
                 leagueName: str,
                 fullName: str,
                 wins: int,
                 losses: int,
                 roster: UserRoster,
                 overflowFLag: bool = False,
                 overflowPos: str = "") -> None:
        
        self.teamName = teamName
        self.leagueName = leagueName
        self.fullName = fullName
        self.wins = wins
        self.losses = losses
        self.roster = roster
        self.overflowFlag = overflowFLag
        self.overflowPos = overflowPos

    @property
    def teamName(self) -> str:
        """
        Get the team name.
        """
        return self._teamName

    @teamName.setter
    def teamName(self, teamName: str) -> None:
        """
        Set the team name.
        """
        self._teamName = teamName

    @property
    def leagueName(self) -> str:
        """
        Get the league name.
        """
        return self._leagueName

    @leagueName.setter
    def leagueName(self, leagueName: str) -> None:
        """
        Set the league name.
        """
        self._leagueName = leagueName

    @property
    def fullName(self) -> str:
        """
        Get the user name.
        """
        return self._fullName

    @fullName.setter
    def fullName(self, fullName: str) -> None:
        """
        Set the user name.
        """
        self._fullName = fullName

    @property
    def wins(self) -> int:
        """
        Get the number of wins.
        """
        return self._wins

    @wins.setter
    def wins(self, wins: int) -> None:
        """
        Set the number of wins.
        """
        self._wins = wins

    @property
    def losses(self) -> int:
        """
        Get the number of losses.
        """
        return self._losses

    @losses.setter
    def losses(self, losses: int) -> None:
        """
        Set the number of losses.
        """
        self._losses = losses

    @property
    def roster(self) -> UserRoster:
        """
        Get the user roster.
        """
        return self._roster

    @roster.setter
    def roster(self, roster: UserRoster) -> None:
        """
        Set the user roster.
        """
        self._roster = roster

    @property
    def overflowFlag(self) -> bool:
        """
        Get the overflow flag.
        """
        return self._overflowFlag
    
    @overflowFlag.setter
    def overflowFlag(self, overflowFlag: bool) -> None:
        """
        Set the overflow flag.
        """
        self._overflowFlag = overflowFlag

    @property
    def overflowPos(self) -> str:
        """
        Get the overflow position.
        """
        return self._overflowPos
    
    @overflowPos.setter
    def overflowPos(self, overflowPos: str) -> None:
        """
        Set the overflow position.
        """
        self._overflowPos = overflowPos
        
    def toJson(self) -> str:
        """
        Convert the object to a JSON string.
        """
        return {
            'teamName': self.teamName,
            'leagueName': self.leagueName,
            'fullName': self.fullName,
            'wins': self.wins,
            'losses': self.losses,
            'roster': self.roster.to_json(),
            'overflowFlag': self.overflowFlag,
            'overflowPos': self.overflowPos
        }
