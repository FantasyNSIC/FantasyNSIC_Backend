"""This class represents a waiver wire claim in a league."""
from .NSIC_Player import NSIC_Player


class Waiver_Wire_Claim:
    """
    A waiver wire claim representation in the database.
    """
    def __init__(self,
                 added_player: NSIC_Player,
                 dropped_player) -> None:
        """
        Initializes a waiver wire claim object.
        """
        self.added_player = added_player
        self.dropped_player = dropped_player
    
    @property
    def added_player(self) -> NSIC_Player:
        """
        Returns the player being added.
        """
        return self._added_player
    
    @added_player.setter
    def added_player(self, added_player: NSIC_Player) -> None:
        """
        Sets the player being added.
        """
        self._added_player = added_player

    @property
    def dropped_player(self):
        """
        Returns the player being dropped, can be null.
        """
        return self._dropped_player
    
    @dropped_player.setter
    def dropped_player(self, dropped_player):
        """
        Sets the player being dropped, can be null.
        """
        self._dropped_player = dropped_player

    def to_json(self) -> dict:
        """
        Converts the waiver wire claim object to a JSON object.
        """
        if self.dropped_player is None:
            return {
                'added_player': self.added_player.to_json(),
                'dropped_player': None
            }
        return {
            'added_player': self.added_player.to_json(),
            'dropped_player': self.dropped_player.to_json()
        }
    
    @staticmethod
    def from_json(json: dict):
        """
        Converts a JSON object to a waiver wire claim object.
        """
        if json['dropped_player'] is None:
            return Waiver_Wire_Claim(
                NSIC_Player.from_json(json['added_player']),
                None
            )
        return Waiver_Wire_Claim(
            NSIC_Player.from_json(json['added_player']),
            NSIC_Player.from_json(json['dropped_player'])
        )
    
    @classmethod
    def from_tuple(cls, tuple: tuple) -> "Waiver_Wire_Claim":
        """
        Converts a tuple to a waiver wire claim object.
        """
        if tuple[9] is None:
            return Waiver_Wire_Claim(
                NSIC_Player.from_tuple(tuple[0:9]),
                None
            )
        return Waiver_Wire_Claim(
            NSIC_Player.from_tuple(tuple[0:9]),
            NSIC_Player.from_tuple(tuple[9:])
        )
