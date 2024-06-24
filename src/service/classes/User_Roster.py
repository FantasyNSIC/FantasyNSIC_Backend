"""This class is a representation of a user's roster. It contains a list
   of players within their respective spots on the roster."""

import json
from .NSIC_Player import NSIC_Player

class UserRoster:
    def __init__(self):
        self.QB = []
        self.RB = []
        self.WR = []
        self.TE = []
        self.K = []
        self.BENCH = []

    def add_player(self, player: NSIC_Player, position: str) -> None:
        """
        Adds a player to the roster.
        :param player: The player to add.
        :param position: The position of the player.
        """
        if position == 'QB':
            self.QB.append(player)
        elif position == 'RB':
            self.RB.append(player)
        elif position == 'WR':
            self.WR.append(player)
        elif position == 'TE':
            self.TE.append(player)
        elif position == 'K':
            self.K.append(player)
        elif position == 'BENCH':
            self.BENCH.append(player)

    def add_empty_player(self, position: str) -> None:
        """
        Adds an empty player to the roster.
        :param position: The position of the player.
        """
        self.add_player(NSIC_Player.empty_player(), position)

    def remove_player(self, player: NSIC_Player) -> None:
        """
        Removes a player from the roster.
        :param player: The player to remove.
        """
        if player in self.QB:
            self.QB.remove(player)
        elif player in self.RB:
            self.RB.remove(player)
        elif player in self.WR:
            self.WR.remove(player)
        elif player in self.TE:
            self.TE.remove(player)
        elif player in self.K:
            self.K.remove(player)
        elif player in self.BENCH:
            self.BENCH.remove(player)

    def to_json(self) -> dict:
        """
        Returns a dictionary representation of the roster.
        """
        return {
            "QB": [player.to_json() for player in self.QB],
            "RB": [player.to_json() for player in self.RB],
            "WR": [player.to_json() for player in self.WR],
            "TE": [player.to_json() for player in self.TE],
            "K": [player.to_json() for player in self.K],
            "BENCH": [player.to_json() for player in self.BENCH]
        }
    
    def from_json(self, json_data: dict) -> None:
        """
        Initializes the roster from a dictionary.
        :param json_data: The dictionary to initialize from.
        """
        self.QB = [NSIC_Player.from_json(player) for player in json_data["QB"]]
        self.RB = [NSIC_Player.from_json(player) for player in json_data["RB"]]
        self.WR = [NSIC_Player.from_json(player) for player in json_data["WR"]]
        self.TE = [NSIC_Player.from_json(player) for player in json_data["TE"]]
        self.K = [NSIC_Player.from_json(player) for player in json_data["K"]]
        self.BENCH = [NSIC_Player.from_json(player) for player in json_data["BENCH"]]
