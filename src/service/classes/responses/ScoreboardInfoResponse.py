"""This class represents a response object for the scoreboard information."""
from ..Week_Matchup import Week_Matchup


class ScoreboardInfoResponse:
    """
    Represents a response object for the scoreboard information, weekly matchups.
    """
    def __init__(self,
                 league_name: str,
                 current_week: str,
                 matchups: list) -> None:
        """
        Initializes a scoreboard information response object.
        """
        self.league_name = league_name
        self.current_week = current_week
        self.matchups = matchups

    @property
    def league_name(self) -> str:
        """
        Returns the league name.
        """
        return self._league_name
    
    @league_name.setter
    def league_name(self, league_name: str) -> None:
        """
        Sets the league name.
        """
        if not isinstance(league_name, str):
            raise ValueError("League name must be a string.")
        self._league_name = league_name

    @property
    def current_week(self) -> str:
        """
        Returns the current week.
        """
        return self._current_week
    
    @current_week.setter
    def current_week(self, current_week: str) -> None:
        """
        Sets the current week.
        """
        if not isinstance(current_week, str):
            raise ValueError("Current week must be a string.")
        self._current_week = current_week

    @property
    def matchups(self) -> list:
        """
        Returns the weekly matchups.
        """
        return self._matchups
    
    @matchups.setter
    def matchups(self, matchups: list) -> None:
        """
        Sets the weekly matchups.
        """
        if not all(isinstance(matchup, Week_Matchup) for matchup in matchups):
            raise ValueError("Matchups must be a list of Week_Matchup objects.")
        self._matchups = matchups


    def toJson(self):
        """
        Returns the JSON representation of the object.
        """
        return {
            "league_name": self.league_name,
            "current_week": self.current_week,
            "matchups": [matchup.to_json() for matchup in self.matchups]
        }
    
    @staticmethod
    def fromJson(json: dict) -> 'ScoreboardInfoResponse':
        """
        Returns a ScoreboardInfoResponse object from a JSON object.
        """
        return ScoreboardInfoResponse(
            league_name=json["league_name"],
            current_week=json["current_week"],
            matchups=[Week_Matchup.from_json(matchup) for matchup in json["matchups"]]
        )
