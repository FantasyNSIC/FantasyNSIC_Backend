"""
This class containes the representation of general player information
stored in the database.
"""


class NSIC_Player:
    """
    Represents a player in the database.
    """
    def __init__(self,
                 player_id: int,
                 first_name: str,
                 last_name: str,
                 team_id: int,
                 pos: str,
                 cls: str,
                 jersey_number: int,
                 height: str,
                 weight: int,
                 total_points: float = 0.0) -> None:
        """
        Initializes a player object.
        """
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.team_id = team_id
        self.pos = pos
        self.cls = cls
        self.jersey_number = jersey_number
        self.height = height
        self.weight = weight
        self.total_points = total_points
        
    @property
    def player_id(self) -> int:
        """
        Returns the player's id.
        """
        return self._player_id
        
    @player_id.setter
    def player_id(self, player_id: int) -> None:
        """
        Sets the player's id.
        """
        if not isinstance(player_id, int):
            raise ValueError("Player ID must be an integer.")
        self._player_id = player_id

    @property
    def first_name(self) -> str:
        """
        Returns the player's first name.
        """
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """
        Sets the player's first name.
        """
        if not isinstance(first_name, str):
            raise ValueError("First name must be a string.")
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """
        Returns the player's last name.
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """
        Sets the player's last name.
        """
        if not isinstance(last_name, str):
            raise ValueError("Last name must be a string.")
        self._last_name = last_name

    @property
    def team_id(self) -> int:
        """
        Returns the player's team id.
        """
        return self._team_id
    
    @team_id.setter
    def team_id(self, team_id: int) -> None:
        """
        Sets the player's team id.
        """
        if not isinstance(team_id, int):
            raise ValueError("Team ID must be an integer.")
        self._team_id = team_id

    @property
    def pos(self) -> str:
        """
        Returns the player's position.
        """
        return self._pos
    
    @pos.setter
    def pos(self, pos: str) -> None:
        """
        Sets the player's position.
        """
        if not isinstance(pos, str):
            raise ValueError("Position must be a string.")
        self._pos = pos

    @property
    def cls(self) -> str:
        """
        Returns the player's class.
        """
        return self._cls
    
    @cls.setter
    def cls(self, cls: str) -> None:
        """
        Sets the player's class.
        """
        if not isinstance(cls, str):
            raise ValueError("Class must be a string.")
        self._cls = cls

    @property
    def jersey_number(self) -> int:
        """
        Returns the player's jersey number.
        """
        return self._jersey_number
    
    @jersey_number.setter
    def jersey_number(self, jersey_number: int) -> None:
        """
        Sets the player's jersey number.
        """
        if not isinstance(jersey_number, int):
            raise ValueError("Jersey number must be a integer.")
        self._jersey_number = jersey_number

    @property
    def height(self) -> str:
        """
        Returns the player's height.
        """
        return self._height
    
    @height.setter
    def height(self, height: str) -> None:
        """
        Sets the player's height.
        """
        if not isinstance(height, str):
            raise ValueError("Height must be an string.")
        self._height = height

    @property
    def weight(self) -> int:
        """
        Returns the player's weight.
        """
        return self._weight
    
    @weight.setter
    def weight(self, weight: int) -> None:
        """
        Sets the player's weight.
        """
        if not isinstance(weight, int):
            raise ValueError("Weight must be an integer.")
        self._weight = weight

    @property
    def total_points(self) -> float:
        """
        Returns the player's total points.
        """
        return self._total_points
    
    @total_points.setter
    def total_points(self, total_points: float) -> None:
        """
        Sets the player's total points.
        """
        if not isinstance(total_points, float):
            raise ValueError("Total points must be a float.")
        self._total_points = total_points

    @classmethod
    def empty_player(cls) -> "NSIC_Player":
        """
        Returns an empty player object.
        """
        return cls(
            player_id=0,
            first_name="",
            last_name="",
            team_id=0,
            pos="",
            cls="",
            jersey_number=0,
            height="",
            weight=0
        )

    def to_json(self) -> dict:
        """
        Returns a JSON representation of the player.
        """
        return {
            "player_id": self.player_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "team_id": self.team_id,
            "pos": self.pos,
            "cls": self.cls,
            "jersey_number": self.jersey_number,
            "height": self.height,
            "weight": self.weight,
            "total_points": self.total_points
        }
    
    def to_dict(self):
        """
        Convert the player to a dictionary.

        Returns:
            dict: The dictionary representation of the player.
        """
        return self.__dict__
    
    @classmethod
    def from_json(cls, json: dict) -> "NSIC_Player":
        """
        Returns a player object from a JSON representation.
        """
        return cls(
            player_id=json["player_id"],
            first_name=json["first_name"],
            last_name=json["last_name"],
            team_id=json["team_id"],
            pos=json["pos"],
            cls=json["cls"],
            jersey_number=json["jersey_number"],
            height=json["height"],
            weight=json["weight"],
            total_points=json["total_points"]
        )
    
    @classmethod
    def from_tuple(cls, tuple: tuple) -> "NSIC_Player":
        """
        Returns a player object from a tuple representation.
        """
        return cls(
            player_id=tuple[0],
            first_name=tuple[1],
            last_name=tuple[2],
            team_id=tuple[3],
            pos=tuple[4],
            cls=tuple[5],
            jersey_number=tuple[6],
            height=tuple[7],
            weight=tuple[8],
            total_points=float(tuple[9])
        )
