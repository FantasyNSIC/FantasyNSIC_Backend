"""
This class contains the representation of a given user-team's season record.
"""


class Team_Record:
    """
    Represents a team's season record.
    """
    def __init__(self,
                 user_team_id: int,
                 wins: int,
                 losses: int,
                 points_for: float,
                 points_against: float,
                 user_team_name: str = "") -> None:
        """
        Initializes a team record object.
        """
        self.user_team_id = user_team_id
        self.wins = wins
        self.losses = losses
        self.points_for = points_for
        self.points_against = points_against
        self.user_team_name = user_team_name

    @property
    def user_team_id(self) -> int:
        """
        Returns the user team's id.
        """
        return self._user_team_id
    
    @user_team_id.setter
    def user_team_id(self, user_team_id: int) -> None:
        """
        Sets the user team's id.
        """
        if not isinstance(user_team_id, int):
            raise ValueError("User team ID must be an integer.")
        self._user_team_id = user_team_id

    @property
    def wins(self) -> int:
        """
        Returns the number of wins.
        """
        return self._wins
    
    @wins.setter
    def wins(self, wins: int) -> None:
        """
        Sets the number of wins.
        """
        if not isinstance(wins, int):
            raise ValueError("Wins must be an integer.")
        self._wins = wins

    @property
    def losses(self) -> int:
        """
        Returns the number of losses.
        """
        return self._losses
    
    @losses.setter
    def losses(self, losses: int) -> None:
        """
        Sets the number of losses.
        """
        if not isinstance(losses, int):
            raise ValueError("Losses must be an integer.")
        self._losses = losses

    @property
    def points_for(self) -> float:
        """
        Returns the total points scored.
        """
        return self._points_for
    
    @points_for.setter
    def points_for(self, points_for: float) -> None:
        """
        Sets the total points scored.
        """
        if not isinstance(points_for, float):
            raise ValueError("Points for must be a float.")
        self._points_for = points_for

    @property
    def points_against(self) -> float:
        """
        Returns the total points against.
        """
        return self._points_against
    
    @points_against.setter
    def points_against(self, points_against: float) -> None:
        """
        Sets the total points against.
        """
        if not isinstance(points_against, float):
            raise ValueError("Points against must be a float.")
        self._points_against = points_against

    @property
    def user_team_name(self) -> str:
        """
        Returns the user team's name.
        """
        return self._user_team_name
    
    @user_team_name.setter
    def user_team_name(self, user_team_name: str) -> None:
        """
        Sets the user team's name.
        """
        if not isinstance(user_team_name, str):
            raise ValueError("User team name must be a string.")
        self._user_team_name = user_team_name

    @classmethod
    def empty_record(cls) -> "Team_Record":
        """
        Returns an empty team record.
        """
        return cls(
            user_team_id=0,
            wins=0,
            losses=0,
            points_for=0.0,
            points_against=0.0)

    def to_json(self) -> dict:
        """
        Returns a JSON representation of the team record.
        """
        if self.user_team_name is not "":
            return {
                'user_team_id': self.user_team_id,
                'wins': self.wins,
                'losses': self.losses,
                'points_for': self.points_for,
                'points_against': self.points_against,
                'user_team_name': self.user_team_name
            }
        return {
            'user_team_id': self.user_team_id,
            'wins': self.wins,
            'losses': self.losses,
            'points_for': self.points_for,
            'points_against': self.points_against
        }
    
    @classmethod
    def from_json(cls, data: dict) -> 'Team_Record':
        """
        Creates a team record object from a JSON object.
        """
        if 'user_team_name' in data:
            return cls(data['user_team_id'],
                   data['wins'],
                   data['losses'],
                   data['points_for'],
                   data['points_against'],
                   data['user_team_name']
            )
        return cls(data['user_team_id'],
                   data['wins'],
                   data['losses'],
                   data['points_for'],
                   data['points_against']
        )
    
    @classmethod
    def from_tuple(cls, data: tuple) -> 'Team_Record':
        """
        Creates a team record object from a tuple.
        """
        if len(data) == 6:
            return cls(data[0], data[1], data[2], float(data[3]), float(data[4]), data[5])
        return cls(data[0], data[1], data[2], float(data[3]), float(data[4]))
