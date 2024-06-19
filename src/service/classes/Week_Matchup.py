"""This class represents a given weekly matchup between two teams in a league."""
from .User_Team import User_Team


class Week_Matchup:
    """
    Weekly matchup storing players and team information.
    """
    def __init__(self,
                 team_1: User_Team,
                 team_2: User_Team,
                 team_1_points: float,
                 team_2_points: float,
                 team_1_wins: int,
                 team_2_wins: int,
                 team_1_losses: int,
                 team_2_losses: int) -> None:
        """
        Initializes a weekly matchup object.
        """
        self.team_1 = team_1
        self.team_2 = team_2
        self.team_1_points = team_1_points
        self.team_2_points = team_2_points
        self.team_1_wins = team_1_wins
        self.team_2_wins = team_2_wins
        self.team_1_losses = team_1_losses
        self.team_2_losses = team_2_losses

    @property
    def team_1(self) -> User_Team:
        """
        Returns the first team.
        """
        return self._team_1
    
    @team_1.setter
    def team_1(self, team_1: User_Team) -> None:
        """
        Sets the first team.
        """
        if not isinstance(team_1, User_Team):
            raise ValueError("Team 1 must be a User_Team object.")
        self._team_1 = team_1

    @property
    def team_2(self) -> User_Team:
        """
        Returns the second team.
        """
        return self._team_2
    
    @team_2.setter
    def team_2(self, team_2: User_Team) -> None:
        """
        Sets the second team.
        """
        if not isinstance(team_2, User_Team):
            raise ValueError("Team 2 must be a User_Team object.")
        self._team_2 = team_2

    @property
    def team_1_points(self) -> float:
        """
        Returns the first team's points.
        """
        return self._team_1_points
    
    @team_1_points.setter
    def team_1_points(self, team_1_points: float) -> None:
        """
        Sets the first team's points.
        """
        if not isinstance(team_1_points, float):
            raise ValueError("Team 1 points must be a float.")
        self._team_1_points = team_1_points

    @property
    def team_2_points(self) -> float:
        """
        Returns the second team's points.
        """
        return self._team_2_points
    
    @team_2_points.setter
    def team_2_points(self, team_2_points: float) -> None:
        """
        Sets the second team's points.
        """
        if not isinstance(team_2_points, float):
            raise ValueError("Team 2 points must be a float.")
        self._team_2_points = team_2_points

    @property
    def team_1_wins(self) -> int:
        """
        Returns the first team's wins.
        """
        return self._team_1_wins
    
    @team_1_wins.setter
    def team_1_wins(self, team_1_wins: int) -> None:
        """
        Sets the first team's wins.
        """
        if not isinstance(team_1_wins, int):
            raise ValueError("Team 1 wins must be an integer.")
        self._team_1_wins = team_1_wins

    @property
    def team_2_wins(self) -> int:
        """
        Returns the second team's wins.
        """
        return self._team_2_wins
    
    @team_2_wins.setter
    def team_2_wins(self, team_2_wins: int) -> None:
        """
        Sets the second team's wins.
        """
        if not isinstance(team_2_wins, int):
            raise ValueError("Team 2 wins must be an integer.")
        self._team_2_wins = team_2_wins

    @property
    def team_1_losses(self) -> int:
        """
        Returns the first team's losses.
        """
        return self._team_1_losses
    
    @team_1_losses.setter
    def team_1_losses(self, team_1_losses: int) -> None:
        """
        Sets the first team's losses.
        """
        if not isinstance(team_1_losses, int):
            raise ValueError("Team 1 losses must be an integer.")
        self._team_1_losses = team_1_losses

    @property
    def team_2_losses(self) -> int:
        """
        Returns the second team's losses.
        """
        return self._team_2_losses
    
    @team_2_losses.setter
    def team_2_losses(self, team_2_losses: int) -> None:
        """
        Sets the second team's losses.
        """
        if not isinstance(team_2_losses, int):
            raise ValueError("Team 2 losses must be an integer.")
        self._team_2_losses = team_2_losses

    def to_json(self) -> dict:
        """
        Returns the weekly matchup as a JSON object.
        """
        return {
            "team_1": self.team_1.to_json(),
            "team_2": self.team_2.to_json(),
            "team_1_points": self.team_1_points,
            "team_2_points": self.team_2_points,
            "team_1_wins": self.team_1_wins,
            "team_2_wins": self.team_2_wins,
            "team_1_losses": self.team_1_losses,
            "team_2_losses": self.team_2_losses
        }
    
    @staticmethod
    def from_json(json: dict) -> 'Week_Matchup':
        """
        Returns a weekly matchup from a JSON object.
        """
        return Week_Matchup(
            User_Team.from_json(json["team_1"]),
            User_Team.from_json(json["team_2"]),
            json["team_1_points"],
            json["team_2_points"],
            json["team_1_wins"],
            json["team_2_wins"],
            json["team_1_losses"],
            json["team_2_losses"]
        )
        
