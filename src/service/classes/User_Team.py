"""
This class represents the user_team table in the database.
"""


class User_Team:
    """
    Represents a user-team for a given league.
    """
    def __init__(self,
                 user_team_id: int,
                 user_id: int,
                 team_name: str,
                 league_id: int,
                 full_name: str = "") -> None:
        """
        Initializes a user-team object.
        """
        self.user_team_id = user_team_id
        self.user_id = user_id
        self.team_name = team_name
        self.league_id = league_id
        self.full_name = full_name

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
    def user_id(self) -> int:
        """
        Returns the user's id.
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id: int) -> None:
        """
        Sets the user's id.
        """
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        self._user_id = user_id

    @property
    def team_name(self) -> str:
        """
        Returns the team name.
        """
        return self._team_name
    
    @team_name.setter
    def team_name(self, team_name: str) -> None:
        """
        Sets the team name.
        """
        if not isinstance(team_name, str):
            raise ValueError("Team name must be a string.")
        self._team_name = team_name

    @property
    def league_id(self) -> int:
        """
        Returns the league id.
        """
        return self._league_id
    
    @league_id.setter
    def league_id(self, league_id: int) -> None:
        """
        Sets the league id.
        """
        if not isinstance(league_id, int):
            raise ValueError("League ID must be an integer.")
        self._league_id = league_id

    @property
    def full_name(self) -> str:
        """
        Returns the full name of the user.
        """
        return self._full_name
    
    @full_name.setter
    def full_name(self, full_name: str) -> None:
        """
        Sets the full name of the user.
        """
        if not isinstance(full_name, str):
            raise ValueError("Full name must be a string.")
        self._full_name = full_name

    def to_json(self) -> dict:
        """
        Returns a dictionary representation of the user-team object.
        """
        if self.full_name is not "":
            return {
                "user_team_id": self.user_team_id,
                "user_id": self.user_id,
                "team_name": self.team_name,
                "league_id": self.league_id,
                "full_name": self.full_name
            }
        return {
            "user_team_id": self.user_team_id,
            "user_id": self.user_id,
            "team_name": self.team_name,
            "league_id": self.league_id
        }
    
    @classmethod
    def from_json(json: dict) -> "User_Team":
        """
        Returns a user-team object from a dictionary.
        """
        if "full_name" in json:
            return User_Team(
                json["user_team_id"],
                json["user_id"],
                json["team_name"],
                json["league_id"],
                json["full_name"]
            )
        return User_Team(
            json["user_team_id"],
            json["user_id"],
            json["team_name"],
            json["league_id"]
        )
    
    def from_tuple(data: tuple) -> "User_Team":
        """
        Returns a user-team object from a tuple.
        """
        if len(data) == 4 or data[4] is None:
            return User_Team(
                data[0],
                data[1],
                data[2],
                data[3]
            )
        return User_Team(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4]
        )
