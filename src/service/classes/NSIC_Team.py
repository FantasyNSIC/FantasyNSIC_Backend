"""
This class represents a NSIC team in the database.
"""


class NSIC_Team:
    """
    Represents a team in the database.
    """
    def __init__(self,
                 team_id: int,
                 team_name: str,
                 abr: str) -> None:
        """
        Initializes a team object.
        """
        self.team_id = team_id
        self.team_name = team_name
        self.abr = abr

    @property
    def team_id(self) -> int:
        """
        Returns the team's id.
        """
        return self._team_id
    
    @team_id.setter
    def team_id(self, team_id: int) -> None:
        """
        Sets the team's id.
        """
        if not isinstance(team_id, int):
            raise ValueError("Team ID must be an integer.")
        self._team_id = team_id

    @property
    def team_name(self) -> str:
        """
        Returns the team's name.
        """
        return self._team_name
    
    @team_name.setter
    def team_name(self, team_name: str) -> None:
        """
        Sets the team's name.
        """
        if not isinstance(team_name, str):
            raise ValueError("Team name must be a string.")
        self._team_name = team_name

    @property
    def abr(self) -> str:
        """
        Returns the team's abbreviation.
        """
        return self._abr
    
    @abr.setter
    def abr(self, abr: str) -> None:
        """
        Sets the team's abbreviation.
        """
        if not isinstance(abr, str):
            raise ValueError("Team abbreviation must be a string.")
        self._abr = abr

    @classmethod
    def empty_team(cls) -> 'NSIC_Team':
        """
        Returns an empty team object.
        """
        return cls(
            team_id=0,
            team_name='',
            abr=''
        )

    def to_json(self) -> dict:
        """
        Converts the team object to a JSON object.
        """
        return {
            "team_id": self.team_id,
            "team_name": self.team_name,
            "abr": self.abr
        }
    
    @classmethod
    def from_json(cls, json: dict) -> 'NSIC_Team':
        """
        Converts a JSON object to a team object.
        """
        return cls(
            team_id=json['team_id'],
            team_name=json['team_name'],
            abr=json['abr']
        )
    
    @classmethod
    def from_tuple(cls, tup: tuple) -> 'NSIC_Team':
        """
        Converts a tuple to a team object.
        """
        return cls(
            team_id=tup[0],
            team_name=tup[1],
            abr=tup[2]
        )
