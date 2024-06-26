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
    
    @player_id.setter
    def player_id(self, player_id: int) -> None:
        """
        Sets the player's id.
        """
        if not isinstance(player_id, int):
            raise ValueError("Player ID must be an integer.")
        self._player_id = player_id
    
    @property
    def gp(self) -> int:
        """
        Returns the number of games played.
        """
        return self._gp
    
    @gp.setter
    def gp(self, gp: int) -> None:
        """
        Sets the number of games played.
        """
        if not isinstance(gp, int):
            raise ValueError("Games played must be an integer.")
        self._gp = gp
    
    @property
    def rush_att(self) -> int:
        """
        Returns the number of rushing attempts.
        """
        return self._rush_att
    
    @rush_att.setter
    def rush_att(self, rush_att: int) -> None:
        """
        Sets the number of rushing attempts.
        """
        if not isinstance(rush_att, int):
            raise ValueError("Rushing attempts must be an integer.")
        self._rush_att = rush_att
    
    @property
    def rush_yds(self) -> int:
        """
        Returns the number of rushing yards.
        """
        return self._rush_yds
    
    @rush_yds.setter
    def rush_yds(self, rush_yds: int) -> None:
        """
        Sets the number of rushing yards.
        """
        if not isinstance(rush_yds, int):
            raise ValueError("rush_yds must be an integer")
        self._rush_yds = rush_yds
    
    @property
    def rush_avg(self) -> float:
        """
        Returns the average rushing yards per attempt.
        """
        return self._rush_avg
    
    @rush_avg.setter
    def rush_avg(self, rush_avg: float) -> None:
        """
        Sets the average rushing yards per attempt.
        """
        if not isinstance(rush_avg, float):
            raise ValueError("rush_avg must be a float")
        self._rush_avg = rush_avg
    
    @property
    def rush_td(self) -> int:
        """
        Returns the number of rushing touchdowns.
        """
        return self._rush_td
    
    @rush_td.setter
    def rush_td(self, rush_td: int) -> None:
        """
        Sets the number of rushing touchdowns.
        """
        if not isinstance(rush_td, int):
            raise ValueError("rush_td must be an integer")
        self._rush_td = rush_td
    
    @property
    def pass_comp(self) -> int:
        """
        Returns the number of passing completions.
        """
        return self._pass_comp
    
    @pass_comp.setter
    def pass_comp(self, pass_comp: int) -> None:
        """
        Sets the number of passing completions.
        """
        if not isinstance(pass_comp, int):
            raise ValueError("pass_comp must be an integer")
        self._pass_comp = pass_comp
    
    @property
    def pass_att(self) -> int:
        """
        Returns the number of passing attempts.
        """
        return self._pass_att
    
    @pass_att.setter
    def pass_att(self, pass_att: int) -> None:
        """
        Sets the number of passing attempts.
        """
        if not isinstance(pass_att, int):
            raise ValueError("pass_att must be an integer")
        self._pass_att = pass_att
    
    @property
    def pass_yds(self) -> int:
        """
        Returns the number of passing yards.
        """
        return self._pass_yds
    
    @pass_yds.setter
    def pass_yds(self, pass_yds: int) -> None:
        """
        Sets the number of passing yards.
        """
        if not isinstance(pass_yds, int):
            raise ValueError("pass_yds must be an integer")
        self._pass_yds = pass_yds
    
    @property
    def pass_td(self) -> int:
        """
        Returns the number of passing touchdowns.
        """
        return self._pass_td
    
    @pass_td.setter
    def pass_td(self, pass_td: int) -> None:
        """
        Sets the number of passing touchdowns.
        """
        if not isinstance(pass_td, int):
            raise ValueError("pass_td must be an integer")
        self._pass_td = pass_td
    
    @property
    def pass_int(self) -> int:
        """
        Returns the number of passing interceptions.
        """
        return self._pass_int
    
    @pass_int.setter
    def pass_int(self, pass_int: int) -> None:
        """
        Sets the number of passing interceptions.
        """
        if not isinstance(pass_int, int):
            raise ValueError("pass_int must be an integer")
        self._pass_int = pass_int
    
    @property
    def recieve_rec(self) -> int:
        """
        Returns the number of receptions.
        """
        return self._recieve_rec
    
    @recieve_rec.setter
    def recieve_rec(self, recieve_rec: int) -> None:
        """
        Sets the number of receptions.
        """
        if not isinstance(recieve_rec, int):
            raise ValueError("recieve_rec must be an integer")
        self._recieve_rec = recieve_rec
    
    @property
    def recieve_yds(self) -> int:
        """
        Returns the number of receiving yards.
        """
        return self._recieve_yds
    
    @recieve_yds.setter
    def recieve_yds(self, recieve_yds: int) -> None:
        """
        Sets the number of receiving yards.
        """
        if not isinstance(recieve_yds, int):
            raise ValueError("recieve_yds must be an integer")
        self._recieve_yds = recieve_yds
    
    @property
    def recieve_avg(self) -> float:
        """
        Returns the average receiving yards per reception.
        """
        return self._recieve_avg
    
    @recieve_avg.setter
    def recieve_avg(self, recieve_avg: float) -> None:
        """
        Sets the average receiving yards per reception.
        """
        if not isinstance(recieve_avg, float):
            raise ValueError("recieve_avg must be a float")
        self._recieve_avg = recieve_avg
    
    @property
    def recieve_td(self) -> int:
        """
        Returns the number of receiving touchdowns.
        """
        return self._recieve_td
    
    @recieve_td.setter
    def recieve_td(self, recieve_td: int) -> None:
        """
        Sets the number of receiving touchdowns.
        """
        if not isinstance(recieve_td, int):
            raise ValueError("recieve_td must be an integer")
        self._recieve_td = recieve_td
    
    @property
    def fg_att(self) -> int:
        """
        Returns the number of field goal attempts.
        """
        return self._fg_att
    
    @fg_att.setter
    def fg_att(self, fg_att: int) -> None:
        """
        Sets the number of field goal attempts.
        """
        if not isinstance(fg_att, int):
            raise ValueError("fg_att must be an integer")
        self._fg_att = fg_att
    
    @property
    def fg_made(self) -> int:
        """
        Returns the number of field goals made.
        """
        return self._fg_made
    
    @fg_made.setter
    def fg_made(self, fg_made: int) -> None:
        """
        Sets the number of field goals made.
        """
        if not isinstance(fg_made, int):
            raise ValueError("fg_made must be an integer")
        self._fg_made = fg_made
    
    @classmethod
    def empty_stats(cls, player_id: int) -> "Player_Stats_2023":
        """
        Returns an empty player statistics object.
        """
        return cls(
            player_id=player_id,
            gp=0,
            rush_att=0,
            rush_yds=0,
            rush_avg=0.0,
            rush_td=0,
            pass_comp=0,
            pass_att=0,
            pass_yds=0,
            pass_td=0,
            pass_int=0,
            recieve_rec=0,
            recieve_yds=0,
            recieve_avg=0.0,
            recieve_td=0,
            fg_att=0,
            fg_made=0
        )
    
    def filter_stats(self, pos: str) -> dict:
        """
        Returns the player's statistics based on their position.
        """
        if pos == "RB":
            return {
                "gp": self.gp,
                "rush_att": self.rush_att,
                "rush_yds": self.rush_yds,
                "rush_avg": self.rush_avg,
                "rush_td": self.rush_td,
                "recieve_rec": self.recieve_rec,
                "recieve_yds": self.recieve_yds,
                "recieve_avg": self.recieve_avg,
                "recieve_td": self.recieve_td
            }
        elif pos == "QB":
            return {
                "gp": self.gp,
                "pass_comp": self.pass_comp,
                "pass_att": self.pass_att,
                "pass_yds": self.pass_yds,
                "pass_td": self.pass_td,
                "pass_int": self.pass_int,
                "rush_att": self.rush_att,
                "rush_yds": self.rush_yds,
                "rush_avg": self.rush_avg,
                "rush_td": self.rush_td
            }
        elif pos == "WR":
            return {
                "gp": self.gp,
                "recieve_rec": self.recieve_rec,
                "recieve_yds": self.recieve_yds,
                "recieve_avg": self.recieve_avg,
                "recieve_td": self.recieve_td,
                "rush_att": self.rush_att,
                "rush_yds": self.rush_yds,
                "rush_avg": self.rush_avg,
                "rush_td": self.rush_td
            }
        elif pos == "TE":
            return {
                "gp": self.gp,
                "recieve_rec": self.recieve_rec,
                "recieve_yds": self.recieve_yds,
                "recieve_avg": self.recieve_avg,
                "recieve_td": self.recieve_td,
                "rush_att": self.rush_att,
                "rush_yds": self.rush_yds,
                "rush_avg": self.rush_avg,
                "rush_td": self.rush_td
            }
        elif pos == "K":
            return {
                "gp": self.gp,
                "fg_att": self.fg_att,
                "fg_made": self.fg_made
            }
        else:
            return {
                "gp": self.gp
            }
    
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
    
    @classmethod
    def from_tuple(cls, tup: tuple) -> "Player_Stats_2023":
        """
        Returns a player statistics object from a tuple.
        """
        return cls(
            player_id=tup[0],
            gp=tup[1],
            rush_att=tup[2],
            rush_yds=tup[3],
            rush_avg=float(tup[4]),
            rush_td=tup[5],
            pass_comp=tup[6],
            pass_att=tup[7],
            pass_yds=tup[8],
            pass_td=tup[9],
            pass_int=tup[10],
            recieve_rec=tup[11],
            recieve_yds=tup[12],
            recieve_avg=float(tup[13]),
            recieve_td=tup[14],
            fg_att=tup[15],
            fg_made=tup[16]
        )
