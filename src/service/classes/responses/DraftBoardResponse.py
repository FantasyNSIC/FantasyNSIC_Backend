"""This class represents a response object for the draft board."""
from ..User_Roster import UserRoster


class DraftBoardResponse:
    """
    Represents a response object for the draft board.
    """
    def __init__(self,
                 draft_order: list,
                 available_players: list,
                 user_roster: UserRoster,
                 draft_enable: bool) -> None:
        """
        Initializes a draft board response object.
        """
        self.draft_order = draft_order
        self.available_players = available_players
        self.user_roster = user_roster
        self.draft_enable = draft_enable

    @property
    def draft_order(self) -> list:
        """
        Returns the draft order.
        """
        return self._draft_order
    
    @draft_order.setter
    def draft_order(self, draft_order: list) -> None:
        """
        Sets the draft order.
        """
        if not isinstance(draft_order, list):
            raise ValueError("Draft order must be a list.")
        self._draft_order = draft_order

    @property
    def available_players(self) -> list:
        """
        Returns the available players.
        """
        return self._available_players
    
    @available_players.setter
    def available_players(self, available_players: list) -> None:
        """
        Sets the available players.
        """
        if not isinstance(available_players, list):
            raise ValueError("Available players must be an list.")
        self._available_players = available_players

    @property
    def user_roster(self) -> UserRoster:
        """
        Returns the user roster.
        """
        return self._user_roster
    
    @user_roster.setter
    def user_roster(self, user_roster: UserRoster) -> None:
        """
        Sets the user roster.
        """
        if not isinstance(user_roster, UserRoster):
            raise ValueError("User roster must be a UserRoster object.")
        self._user_roster = user_roster

    @property
    def draft_enable(self) -> bool:
        """
        Returns the draft enable status.
        """
        return self._draft_enable
    
    @draft_enable.setter
    def draft_enable(self, draft_enable: bool) -> None:
        """
        Sets the draft enable status.
        """
        if not isinstance(draft_enable, bool):
            raise ValueError("Draft enable must be a boolean.")
        self._draft_enable = draft_enable

    def toJson(self) -> dict:
        """
        Returns the draft board response as a dictionary.
        """
        return {
            'draft_order': [draft_order.to_json() for draft_order in self.draft_order],
            'available_players': [player.to_json() for player in self.available_players],
            'user_roster': self.user_roster.to_json(),
            'draft_enable': self.draft_enable
        }
