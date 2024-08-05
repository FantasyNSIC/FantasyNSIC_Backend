"""This class represents a database representation of a single draft entry."""
from typing import Optional
from .NSIC_Player import NSIC_Player


class Draft_Order:
    """
    Represents a single draft entry.
    """
    def __init__(self,
                 draft_pick: int,
                 league_id: int,
                 user_team_id: int,
                 team_name: str,
                 player_id: Optional[NSIC_Player] = None) -> None:
        """
        Initializes a draft order object.
        """
        self.draft_pick = draft_pick
        self.league_id = league_id
        self.user_team_id = user_team_id
        self.team_name = team_name
        self.player_id = player_id

    @property
    def draft_pick(self) -> int:
        """
        Returns the draft pick.
        """
        return self._draft_pick
    
    @draft_pick.setter
    def draft_pick(self, draft_pick: int) -> None:
        """
        Sets the draft pick.
        """
        if not isinstance(draft_pick, int):
            raise ValueError("Draft pick must be an integer.")
        self._draft_pick = draft_pick

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
    def user_team_id(self) -> int:
        """
        Returns the user team id.
        """
        return self._user_team_id
    
    @user_team_id.setter
    def user_team_id(self, user_team_id: int) -> None:
        """
        Sets the user team id.
        """
        if not isinstance(user_team_id, int):
            raise ValueError("User team ID must be an integer.")
        self._user_team_id = user_team_id

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
    def player_id(self) -> Optional[NSIC_Player]:
        """
        Returns the player id.
        """
        return self._player_id
    
    @player_id.setter
    def player_id(self, player_id: Optional[NSIC_Player]) -> None:
        """
        Sets the player id.
        """
        if player_id is not None and not isinstance(player_id, NSIC_Player):
            raise ValueError("Player ID must be an object.")
        self._player_id = player_id

    def to_json(self) -> dict:
        """
        Returns the draft order object as a dictionary.
        """
        if self.player_id is not None:
            return {
                'draft_pick': self._draft_pick,
                'league_id': self._league_id,
                'user_team_id': self._user_team_id,
                'team_name': self._team_name,
                'player_id': self._player_id.to_json()
            }
        else:
            return {
                'draft_pick': self._draft_pick,
                'league_id': self._league_id,
                'user_team_id': self._user_team_id,
                'team_name': self._team_name,
                'player_id': None
            }
        
    @staticmethod
    def from_tuple(draft_order_tuple: tuple) -> 'Draft_Order':
        """
        Creates a draft order object from a tuple.
        """
        if draft_order_tuple[4] is None:
            return Draft_Order(
                draft_order_tuple[0],
                draft_order_tuple[1],
                draft_order_tuple[2],
                draft_order_tuple[3]
            )
        else:
            return Draft_Order(
                draft_order_tuple[0],
                draft_order_tuple[1],
                draft_order_tuple[2],
                draft_order_tuple[3],
                NSIC_Player.from_tuple(draft_order_tuple[4:])
            )
