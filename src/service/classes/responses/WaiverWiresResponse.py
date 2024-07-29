"""This class represent a list of waiver wire claim for a given user."""
import json
from ..Waiver_Wire_Claim import Waiver_Wire_Claim


class WaiverWiresResponse:
    def __init__(self, waiver_wire_claims: list):
        self.waiver_wire_claims = waiver_wire_claims

    @classmethod
    def fromJson(cls, json_str):
        data = json.loads(json_str)
        waiver_wire_claims = [Waiver_Wire_Claim.from_json(claim) for claim in data['waiver_wire_claims']]
        return cls(waiver_wire_claims)

    def toJson(self):
        data = {
            'waiver_wire_claims': [claim.to_json() for claim in self.waiver_wire_claims]
        }
        return json.dumps(data)

    @classmethod
    def from_tuple(cls, tuples: list) -> "WaiverWiresResponse":
        waiver_wire_claims = [Waiver_Wire_Claim.from_tuple(claim_tuple) for claim_tuple in tuples]
        return cls(waiver_wire_claims)