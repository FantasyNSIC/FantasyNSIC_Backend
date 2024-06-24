"""This file caontain response object that holds information about a given week's matchup for a user."""
from ..User_Roster import UserRoster
from ..Team_Record import Team_Record


class MatchupInfoResponse:
    """
    Represents a response object for the matchup information, weekly matchups.
    """
    def __init__(self,
                current_week: str,
                team_1_name: str,
                team_1_full_name: str,
                team_1_record: Team_Record,
                team_1_points: float,
                team_1_roster: UserRoster,
                team_2_name: str,
                team_2_full_name: str,
                team_2_record: Team_Record,
                team_2_points: float,
                team_2_roster: UserRoster) -> None:
        """
        Initializes a matchup response object.
        """
        self.current_week = current_week
        self.team_1_name = team_1_name
        self.team_1_full_name = team_1_full_name
        self.team_1_record = team_1_record
        self.team_1_points = team_1_points
        self.team_1_roster = team_1_roster
        self.team_2_name = team_2_name
        self.team_2_full_name = team_2_full_name
        self.team_2_record = team_2_record
        self.team_2_points = team_2_points
        self.team_2_roster = team_2_roster

    @property
    def current_week(self) -> str:
        """
        Returns the current week.
        """
        return self._current_week
    
    @current_week.setter
    def current_week(self, current_week: str) -> None:
        """
        Sets the current week.
        """
        if not isinstance(current_week, str):
            raise ValueError("Current week must be a string.")
        self._current_week = current_week

    @property
    def team_1_name(self) -> str:
        """
        Returns the team 1 name.
        """
        return self._team_1_name
    
    @team_1_name.setter
    def team_1_name(self, team_1_name: str) -> None:
        """
        Sets the team 1 name.
        """
        if not isinstance(team_1_name, str):
            raise ValueError("Team 1 name must be a string.")
        self._team_1_name = team_1_name

    @property
    def team_1_full_name(self) -> str:
        """
        Returns the team 1 full name.
        """
        return self._team_1_full_name
    
    @team_1_full_name.setter
    def team_1_full_name(self, team_1_full_name: str) -> None:
        """
        Sets the team 1 full name.
        """
        if not isinstance(team_1_full_name, str):
            raise ValueError("Team 1 full name must be a string.")
        self._team_1_full_name = team_1_full_name

    @property
    def team_1_points(self) -> float:
        """
        Returns the team 1 points.
        """
        return self._team_1_points
    
    @team_1_points.setter
    def team_1_points(self, team_1_points: float) -> None:
        """
        Sets the team 1 points.
        """
        if not isinstance(team_1_points, float):
            raise ValueError("Team 1 points must be a float.")
        self._team_1_points = team_1_points

    @property
    def team_1_record(self) -> Team_Record:
        """
        Returns the team 1 record.
        """
        return self._team_1_record
    
    @team_1_record.setter
    def team_1_record(self, team_1_record: Team_Record) -> None:
        """
        Sets the team 1 record.
        """
        if not isinstance(team_1_record, Team_Record):
            raise ValueError("Team 1 record must be a Team_Record object.")
        self._team_1_record = team_1_record

    @property
    def team_1_roster(self) -> UserRoster:
        """
        Returns the team 1 roster.
        """
        return self._team_1_roster
    
    @team_1_roster.setter
    def team_1_roster(self, team_1_roster: UserRoster) -> None:
        """
        Sets the team 1 roster.
        """
        if not isinstance(team_1_roster, UserRoster):
            raise ValueError("Team 1 roster must be a UserRoster object.")
        self._team_1_roster = team_1_roster

    @property
    def team_2_name(self) -> str:
        """
        Returns the team 2 name.
        """
        return self._team_2_name
    
    @team_2_name.setter
    def team_2_name(self, team_2_name: str) -> None:
        """
        Sets the team 2 name.
        """
        if not isinstance(team_2_name, str):
            raise ValueError("Team 2 name must be a string.")
        self._team_2_name = team_2_name

    @property
    def team_2_full_name(self) -> str:
        """
        Returns the team 2 full name.
        """
        return self._team_2_full_name
    
    @team_2_full_name.setter
    def team_2_full_name(self, team_2_full_name: str) -> None:
        """
        Sets the team 2 full name.
        """
        if not isinstance(team_2_full_name, str):
            raise ValueError("Team 2 full name must be a string.")
        self._team_2_full_name = team_2_full_name

    @property
    def team_2_points(self) -> float:
        """
        Returns the team 2 points.
        """
        return self._team_2_points
    
    @team_2_points.setter
    def team_2_points(self, team_2_points: float) -> None:
        """
        Sets the team 2 points.
        """
        if not isinstance(team_2_points, float):
            raise ValueError("Team 2 points must be a float.")
        self._team_2_points = team_2_points

    @property
    def team_2_record(self) -> Team_Record:
        """
        Returns the team 2 record.
        """
        return self._team_2_record
    
    @team_2_record.setter
    def team_2_record(self, team_2_record: Team_Record) -> None:
        """
        Sets the team 2 record.
        """
        if not isinstance(team_2_record, Team_Record):
            raise ValueError("Team 2 record must be a Team_Record object.")
        self._team_2_record = team_2_record

    @property
    def team_2_roster(self) -> UserRoster:
        """
        Returns the team 2 roster.
        """
        return self._team_2_roster
    
    @team_2_roster.setter
    def team_2_roster(self, team_2_roster: UserRoster) -> None:
        """
        Sets the team 2 roster.
        """
        if not isinstance(team_2_roster, UserRoster):
            raise ValueError("Team 2 roster must be a UserRoster object.")
        self._team_2_roster = team_2_roster

    def toJson(self) -> dict:
        """
        Returns a JSON representation of the matchup information response.
        """
        return {
            'current_week': self.current_week,
            'team_1_name': self.team_1_name,
            'team_1_full_name': self.team_1_full_name,
            'team_1_record': self.team_1_record.to_json(),
            'team_1_points': self.team_1_points,
            'team_1_roster': self.team_1_roster.to_json(),
            'team_2_name': self.team_2_name,
            'team_2_full_name': self.team_2_full_name,
            'team_2_record': self.team_2_record.to_json(),
            'team_2_points': self.team_2_points,
            'team_2_roster': self.team_2_roster.to_json()
        }
    
    @staticmethod
    def fromJson(json: dict) -> 'MatchupInfoResponse':
        """
        Returns a MatchupInfoResponse object from a JSON representation.
        """
        return MatchupInfoResponse(
            json['current_week'],
            json['team_1_name'],
            json['team_1_full_name'],
            Team_Record.from_json(json['team_1_record']),
            json['team_1_points'],
            UserRoster.from_json(json['team_1_roster']),
            json['team_2_name'],
            json['team_2_full_name'],
            Team_Record.from_json(json['team_2_record']),
            json['team_2_points'],
            UserRoster.from_json(json['team_2_roster'])
        )
