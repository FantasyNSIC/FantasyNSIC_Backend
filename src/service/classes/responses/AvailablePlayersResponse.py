import json
from ..NSIC_Player import NSIC_Player

class AvailablePlayersResponse:
    def __init__(self, players: list):
        self.players = players

    @classmethod
    def fromJson(cls, json_str):
        data = json.loads(json_str)
        players = [NSIC_Player.from_json(player) for player in data['players']]
        return cls(players)

    def toJson(self):
        data = {
            'players': [player.to_json() for player in self.players]
        }
        return json.dumps(data)

    @classmethod
    def from_tuple(cls, tuples: list) -> "AvailablePlayersResponse":    
        players = [NSIC_Player.from_tuple(player_tuple) for player_tuple in tuples]
        return cls(players)