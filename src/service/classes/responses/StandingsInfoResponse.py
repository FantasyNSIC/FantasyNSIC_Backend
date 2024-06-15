"""
This class contains the functionality of a list of Team_Record objects.
"""
import json
from ..Team_Record import Team_Record


class StandingsInfoResponse:
    """
    Represents a list of Team_Record objects.
    """
    def __init__(self, records: list) -> None:
        """
        Initializes a standings information response object.
        """
        self.records = records

    @property
    def records(self) -> list:
        """
        Returns the list of user records.
        """
        return self._records
    
    @records.setter
    def records(self, records: list) -> None:
        """
        Sets the list of user records.
        """
        if not isinstance(records, list):
            raise ValueError("Records must be a list.")
        self._records = records

    def toJson(self) -> dict:
        """
        Converts the object to a JSON serializable dictionary.
        """
        data = {
            "records": [record.to_json() for record in self.records]
        }
        return json.dumps(data)
    
    @classmethod
    def fromJson(cls, json_str: str) -> "StandingsInfoResponse":
        """
        Creates a StandingsInfoResponse object from a JSON string.
        """
        data = json.loads(json_str)
        records = [Team_Record.from_json(record) for record in data['records']]
        return cls(records)
    
    @classmethod
    def from_tuple(cls, tuples: list) -> "StandingsInfoResponse":
        """
        Creates a StandingsInfoResponse object from a list of tuples.
        """
        records = [Team_Record.from_tuple(record) for record in tuples]
        return cls(records)
