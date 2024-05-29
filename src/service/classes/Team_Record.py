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
                 points_against: float) -> None:
        """
        Initializes a team record object.
        """
        self.user_team_id = user_team_id
        self.wins = wins
        self.losses = losses
        self.points_for = points_for
        self.points_against = points_against

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

    def to_json(self) -> dict:
        """
        Returns a JSON representation of the team record.
        """
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
        return cls(data['user_team_id'],
                   data['wins'],
                   data['losses'],
                   data['points_for'],
                   data['points_against']
        )
