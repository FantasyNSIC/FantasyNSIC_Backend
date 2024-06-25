"""This file contains the response class for returning all related info on a NSIC player."""
from ..NSIC_Player import NSIC_Player
from ..NSIC_Team import NSIC_Team
from ..Player_Stats_Week import Player_Stats_Week
from ..Player_Stats_2023 import Player_Stats_2023


class NSICPlayerResponse:
    """
    Represents a response object for the NSIC player information.
    """
    def __init__(self,
                 player_info: NSIC_Player,
                 player_team: NSIC_Team,
                 stats_2023: Player_Stats_2023,
                 weekly_stats: list) -> None:
        """
        Initializes a NSIC player response object.
        """
        self.player_info = player_info
        self.player_team = player_team
        self.stats_2023 = stats_2023
        self.weekly_stats = weekly_stats

    @property
    def player_info(self) -> NSIC_Player:
        """
        Returns the player's information.
        """
        return self._player_info
    
    @player_info.setter
    def player_info(self, player_info: NSIC_Player) -> None:
        """
        Sets the player's information.
        """
        if not isinstance(player_info, NSIC_Player):
            raise ValueError("Player info must be a NSIC_Player object.")
        self._player_info = player_info

    @property
    def player_team(self) -> NSIC_Team:
        """
        Returns the player's team.
        """
        return self._player_team
    
    @player_team.setter
    def player_team(self, player_team: NSIC_Team) -> None:
        """
        Sets the player's team.
        """
        if not isinstance(player_team, NSIC_Team):
            raise ValueError("Player team must be a NSIC_Team object.")
        self._player_team = player_team

    @property
    def stats_2023(self) -> Player_Stats_2023:
        """
        Returns the player's 2023 statistics.
        """
        return self._stats_2023
    
    @stats_2023.setter
    def stats_2023(self, stats_2023: Player_Stats_2023) -> None:
        """
        Sets the player's 2023 statistics.
        """
        if not isinstance(stats_2023, Player_Stats_2023):
            raise ValueError("Stats 2023 must be a Player_Stats_2023 object.")
        self._stats_2023 = stats_2023

    @property
    def weekly_stats(self) -> list:
        """
        Returns the player's weekly statistics.
        """
        return self._weekly_stats
    
    @weekly_stats.setter
    def weekly_stats(self, weekly_stats: list) -> None:
        """
        Sets the player's weekly statistics.
        """
        if not all(isinstance(stats, Player_Stats_Week) for stats in weekly_stats):
            raise ValueError("All stats in weekly stats must be Player_Stats_Week object.")
        self._weekly_stats = weekly_stats


    def toJson(self) -> dict:
        """
        Returns the response object as a dictionary.
        """
        return {
            "player_info": self.player_info.to_json(),
            "player_team": self.player_team.to_json(),
            "stats_2023": self.stats_2023.to_json(),
            "weekly_stats": [stat.to_json() for stat in self.weekly_stats]
        }
