"""
This class contains the representation of a NSIC player's statistics for a given week.
"""


class Player_Stats_Week:
    """
    Represents a player's statistics for a given week.
    """
    def __init__(self,
                 player_id: int,
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
                 fg_made: int,
                 week_points: float = 0.0) -> None:
        """
        Initializes a player's statistics object.
        """
        self.player_id = player_id
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
        self.week_points = week_points

    @property
    def player_id(self) -> int:
        """
        Returns the player's id.
        """
        return self._player_id
    
    @player_id.setter
    def player_id(self, value: int) -> None:
        """
        Sets the player's id.
        """
        self._player_id = value
    
    @property
    def rush_att(self) -> int:
        """
        Returns the number of rushing attempts.
        """
        return self._rush_att
    
    @rush_att.setter
    def rush_att(self, value: int) -> None:
        """
        Sets the number of rushing attempts.
        """
        self._rush_att = value
    
    @property
    def rush_yds(self) -> int:
        """
        Returns the number of rushing yards.
        """
        return self._rush_yds
    
    @rush_yds.setter
    def rush_yds(self, value: int) -> None:
        """
        Sets the number of rushing yards.
        """
        self._rush_yds = value
    
    @property
    def rush_avg(self) -> float:
        """
        Returns the average rushing yards per attempt.
        """
        return self._rush_avg
    
    @rush_avg.setter
    def rush_avg(self, value: float) -> None:
        """
        Sets the average rushing yards per attempt.
        """
        self._rush_avg = value
    
    @property
    def rush_td(self) -> int:
        """
        Returns the number of rushing touchdowns.
        """
        return self._rush_td
    
    @rush_td.setter
    def rush_td(self, value: int) -> None:
        """
        Sets the number of rushing touchdowns.
        """
        self._rush_td = value
    
    @property
    def pass_comp(self) -> int:
        """
        Returns the number of passing completions.
        """
        return self._pass_comp
    
    @pass_comp.setter
    def pass_comp(self, value: int) -> None:
        """
        Sets the number of passing completions.
        """
        self._pass_comp = value
    
    @property
    def pass_att(self) -> int:
        """
        Returns the number of passing attempts.
        """
        return self._pass_att
    
    @pass_att.setter
    def pass_att(self, value: int) -> None:
        """
        Sets the number of passing attempts.
        """
        self._pass_att = value
    
    @property
    def pass_yds(self) -> int:
        """
        Returns the number of passing yards.
        """
        return self._pass_yds
    
    @pass_yds.setter
    def pass_yds(self, value: int) -> None:
        """
        Sets the number of passing yards.
        """
        self._pass_yds = value
    
    @property
    def pass_td(self) -> int:
        """
        Returns the number of passing touchdowns.
        """
        return self._pass_td
    
    @pass_td.setter
    def pass_td(self, value: int) -> None:
        """
        Sets the number of passing touchdowns.
        """
        self._pass_td = value
    
    @property
    def pass_int(self) -> int:
        """
        Returns the number of passing interceptions.
        """
        return self._pass_int
    
    @pass_int.setter
    def pass_int(self, value: int) -> None:
        """
        Sets the number of passing interceptions.
        """
        self._pass_int = value
    
    @property
    def recieve_rec(self) -> int:
        """
        Returns the number of receptions.
        """
        return self._recieve_rec
    
    @recieve_rec.setter
    def recieve_rec(self, value: int) -> None:
        """
        Sets the number of receptions.
        """
        self._recieve_rec = value
    
    @property
    def recieve_yds(self) -> int:
        """
        Returns the number of receiving yards.
        """
        return self._recieve_yds
    
    @recieve_yds.setter
    def recieve_yds(self, value: int) -> None:
        """
        Sets the number of receiving yards.
        """
        self._recieve_yds = value
    
    @property
    def recieve_avg(self) -> float:
        """
        Returns the average receiving yards per reception.
        """
        return self._recieve_avg
    
    @recieve_avg.setter
    def recieve_avg(self, value: float) -> None:
        """
        Sets the average receiving yards per reception.
        """
        self._recieve_avg = value
    
    @property
    def recieve_td(self) -> int:
        """
        Returns the number of receiving touchdowns.
        """
        return self._recieve_td
    
    @recieve_td.setter
    def recieve_td(self, value: int) -> None:
        """
        Sets the number of receiving touchdowns.
        """
        self._recieve_td = value
    
    @property
    def fg_att(self) -> int:
        """
        Returns the number of field goal attempts.
        """
        return self._fg_att
    
    @fg_att.setter
    def fg_att(self, value: int) -> None:
        """
        Sets the number of field goal attempts.
        """
        self._fg_att = value
    
    @property
    def fg_made(self) -> int:
        """
        Returns the number of field goals made.
        """
        return self._fg_made
    
    @fg_made.setter
    def fg_made(self, value: int) -> None:
        """
        Sets the number of field goals made.
        """
        self._fg_made = value
    
    @property
    def week_points(self) -> float:
        """
        Returns the number of points scored in the week.
        """
        return self._week_points
    
    @week_points.setter
    def week_points(self, value: float) -> None:
        """
        Sets the number of points scored in the week.
        """
        self._week_points = value
    
    def filter_stats(self, pos: str) -> dict:
        """
        Returns the player's statistics based on their position.
        """
        if pos == "RB":
            return {
                "week_points": self.week_points,
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
                "week_points": self.week_points,
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
                "week_points": self.week_points,
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
                "week_points": self.week_points,
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
                "week_points": self.week_points,
                "fg_att": self.fg_att,
                "fg_made": self.fg_made
            }
        else:
            return {
                "week_points": self.week_points,
            }
    
    def to_json(self) -> dict:
        """
        Returns the object as a JSON dictionary.
        """
        return {
            "player_id": self.player_id,
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
            "fg_made": self.fg_made,
            "week_points": self.week_points
        }
    
    @classmethod
    def from_json(cls, json: dict) -> "Player_Stats_Week":
        """
        Returns a player statistics object from a JSON dictionary.
        """
        return cls(
            player_id=json["player_id"],
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
            fg_made=json["fg_made"],
            week_points=json["week_points"]
        )
    
    @classmethod
    def from_tuple(cls, tuple: tuple) -> "Player_Stats_Week":
        """
        Returns a player statistics object from a tuple.
        """
        return cls(
            player_id=tuple[0],
            rush_att=tuple[1],
            rush_yds=tuple[2],
            rush_avg=float(tuple[3]),
            rush_td=tuple[4],
            pass_comp=tuple[5],
            pass_att=tuple[6],
            pass_yds=tuple[7],
            pass_td=tuple[8],
            pass_int=tuple[9],
            recieve_rec=tuple[10],
            recieve_yds=tuple[11],
            recieve_avg=float(tuple[12]),
            recieve_td=tuple[13],
            fg_att=tuple[14],
            fg_made=tuple[15],
            week_points=float(tuple[16])
        )
