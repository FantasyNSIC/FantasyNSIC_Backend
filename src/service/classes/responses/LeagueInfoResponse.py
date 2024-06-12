"""
This class is a response object that contains the information of a league.
"""
from ..User_Team import User_Team


class LeagueInfoResponse:
    """
    League information response object.
    """
    def __init__(self,
                 league_name: str,
                 league_constraint: str,
                 league_teams: list) -> None:
        """
        Initializes a league information response object.
        """
        self.league_name = league_name
        self.league_constraint = league_constraint
        self.league_teams = league_teams
        self.number_of_teams = len(league_teams)

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
    def league_constraint(self) -> str:
        """
        Returns the league constraint.
        """
        return self._league_constraint
    
    @league_constraint.setter
    def league_constraint(self, league_constraint: str) -> None:
        """
        Sets the league constraint.
        """
        if not isinstance(league_constraint, str):
            raise ValueError("League constraint must be a string.")
        self._league_constraint = league_constraint

    @property
    def league_teams(self) -> list:
        """
        Returns the league teams.
        """
        return self._league_teams
    
    @league_teams.setter
    def league_teams(self, league_teams: list) -> None:
        """
        Sets the league teams.
        """
        if not isinstance(league_teams, list):
            raise ValueError("League teams must be a list.")
        self._league_teams = league_teams

    def toJson(self) -> dict:
        """
        Converts the league information response object to a JSON object.
        """
        return {
            'league_name': self.league_name,
            'league_constraint': self.league_constraint,
            'league_teams': [team.to_json() for team in self.league_teams],
            'number_of_teams': self.number_of_teams
        }
    
    @classmethod
    def from_json(cls, json: dict) -> "LeagueInfoResponse":
        """
        Converts a JSON object to a league information response object.
        """
        league_teams = [User_Team.from_json(team) for team in json['league_teams']]
        return cls(json['league_name'], json['league_constraint'], league_teams)
    
    @classmethod
    def from_tuple(cls, tuples: list) -> "LeagueInfoResponse":
        """
        Converts a list of tuples to a league information response object.
        """
        league_teams = [User_Team.from_tuple(team) for team in tuples[1]]
        return cls(tuples[0][0], tuples[0][1], league_teams)
