"""This class is a representation of a user's roster. It contains a list
   of players and their status (active, benched, or injured)."""

import json
from .NSIC_Player import NSIC_Player

class UserRoster:
    def __init__(self):
        self.roster = []

    def add_player(self, player: NSIC_Player, status: str):
        """
        Add a player to the roster with the specified status.

        Args:
            player (NSIC_Player): The player object to add.
            status (str): The status of the player ('active', 'benched', or 'injured').
        """
        self.roster.append({'player': player, 'status': status})

    def remove_player(self, player_id: int):
        """
        Remove a player from the roster.

        Args:
            player_id (NSIC_Player): The player_id from object to remove.
        """
        self.roster = [p for p in self.roster if p['player'].player_id != player_id]

    def to_dict(self):
        """
        Convert the roster to a dictionary.

        Returns:
            dict: The dictionary representation of the roster.
        """
        roster_dict = {i: player.to_dict() for i, player in enumerate(self.roster)}
        return roster_dict

    def toJson(self):
        """
        Convert the roster to a JSON string.

        Returns:
            str: The JSON representation of the roster.
        """
        return [{'player': player['player'].to_json() if hasattr(player['player'], 'to_json') else player['player'],
                 'status': player['status']} for player in self.roster]
    
    @staticmethod
    def from_tuple(tuple):
        """
        Create a UserRoster object from a tuple.

        Args:
            tuple (tuple): The tuple representing the roster.

        Returns:
            UserRoster: The UserRoster object created from the tuple.
        """
        roster = UserRoster()
        for item in tuple:
            player = NSIC_Player.from_tuple(item)
            status = item[1]
            roster.add_player(player, status)
        return roster