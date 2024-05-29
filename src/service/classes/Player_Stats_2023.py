"""
This class contains the representation of a NSIC player's statistics for the 2023 season.
"""


class Player_Stats_2023:
    """
    Represents a player's statistics for the 2023 season.
    """
    def __init__(self,
                 player_id: int,
                 gp: int,
                 rush_att: int,
                 rush_yds: int,
                 rush_avg: float,
                 rush_td: int,
                 pass_comp: int,
                 pass_att: int,
                 pass_yds: int,
                 pass_td: int,
                 pass_int: int,
                 recieve_rec: int,
                 recieve_yds: int,
                 recieve_avg: float,
                 recieve_td: int,
                 fg_att: int,
                 fg_made: int) -> None:
        """
        Initializes a player's statistics object.
        """
        self.player_id = player_id
        self.gp = gp
        self.rush_att = rush_att
        self.rush_yds = rush_yds
        self.rush_avg = rush_avg
        self.rush_td = rush_td
        self.pass_comp = pass_comp
        self.pass_att = pass_att
        self.pass_yds = pass_yds
        self.pass_td = pass_td
        self.pass_int = pass_int
        self.recieve_rec = recieve_rec
        self.recieve_yds = recieve_yds
        self.recieve_avg = recieve_avg
        self.recieve_td = recieve_td
        self.fg_att = fg_att
        self.fg_made = fg_made

    @property
    def player_id(self) -> int:
        """
        Returns the player's id.
        """
        return self._player_id
    
    @property
    def gp(self) -> int:
        """
        Returns the number of games played.
        """
        return self._gp
    
    @property
    def rush_att(self) -> int:
        """
        Returns the number of rushing attempts.
        """
        return self._rush_att
    
    @property
    def rush_yds(self) -> int:
        """
        Returns the number of rushing yards.
        """
        return self._rush_yds
    
    @property
    def rush_avg(self) -> float:
        """
        Returns the average rushing yards per attempt.
        """
        return self._rush_avg
    
    @property
    def rush_td(self) -> int:
        """
        Returns the number of rushing touchdowns.
        """
        return self._rush_td
    
    @property
    def pass_comp(self) -> int:
        """
        Returns the number of passing completions.
        """
        return self._pass_comp
    
    @property
    def pass_att(self) -> int:
        """
        Returns the number of passing attempts.
        """
        return self._pass_att
    
    @property
    def pass_yds(self) -> int:
        """
        Returns the number of passing yards.
        """
        return self._pass_yds
    
    @property
    def pass_td(self) -> int:
        """
        Returns the number of passing touchdowns.
        """
        return self._pass_td
    
    @property
    def pass_int(self) -> int:
        """
        Returns the number of passing interceptions.
        """
        return self._pass_int
    
    @property
    def recieve_rec(self) -> int:
        """
        Returns the number of receptions.
        """
        return self._recieve_rec
    
    @property
    def recieve_yds(self) -> int:
        """
        Returns the number of receiving yards.
        """
        return self._recieve_yds
    
    @property
    def recieve_avg(self) -> float:
        """
        Returns the average receiving yards per reception.
        """
        return self._recieve_avg
    
    @property
    def recieve_td(self) -> int:
        """
        Returns the number of receiving touchdowns.
        """
        return self._recieve_td
    
    @property
    def fg_att(self) -> int:
        """
        Returns the number of field goal attempts.
        """
        return self._fg_att
    
    @property
    def fg_made(self) -> int:
        """
        Returns the number of field goals made.
        """
        return self._fg_made
    
    def to_json(self) -> dict:
        """
        Returns the object as a JSON dictionary.
        """
        return {
            "player_id": self.player_id,
            "gp": self.gp,
            "rush_att": self.rush_att,
            "rush_yds": self.rush_yds,
            "rush_avg": self.rush_avg,
            "rush_td": self.rush_td,
            "pass_comp": self.pass_comp,
            "pass_att": self.pass_att,
            "pass_yds": self.pass_yds,
            "pass_td": self.pass_td,
            "pass_int": self.pass_int,
            "recieve_rec": self.recieve_rec,
            "recieve_yds": self.recieve_yds,
            "recieve_avg": self.recieve_avg,
            "recieve_td": self.recieve_td,
            "fg_att": self.fg_att,
            "fg_made": self.fg_made
        }
    
    @classmethod
    def from_json(cls, json: dict) -> "Player_Stats_2023":
        """
        Returns a player statistics object from a JSON dictionary.
        """
        return cls(
            player_id=json["player_id"],
            gp=json["gp"],
            rush_att=json["rush_att"],
            rush_yds=json["rush_yds"],
            rush_avg=json["rush_avg"],
            rush_td=json["rush_td"],
            pass_comp=json["pass_comp"],
            pass_att=json["pass_att"],
            pass_yds=json["pass_yds"],
            pass_td=json["pass_td"],
            pass_int=json["pass_int"],
            recieve_rec=json["recieve_rec"],
            recieve_yds=json["recieve_yds"],
            recieve_avg=json["recieve_avg"],
            recieve_td=json["recieve_td"],
            fg_att=json["fg_att"],
            fg_made=json["fg_made"]
        )
