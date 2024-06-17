"""
This class holds the constraints for a league. It contains the number of positions
each team is allowed. It also contains the number of players each team is allowed
"""

class LeagueConstraint:
    def __init__(self,
                 qb: int,
                 rb: int,
                 wr: int,
                 te: int,
                 k: int,
                 bench: int):
        self.qb = qb
        self.rb = rb
        self.wr = wr
        self.te = te
        self.k = k
        self.bench = bench

    @property
    def qb(self):
        """
        Get the qb number.
        """
        return self._qb
    
    @qb.setter
    def qb(self, qb):
        """
        Set the qb number.
        """
        self._qb = qb

    @property
    def rb(self):
        """
        Get the rb number.
        """
        return self._rb
    
    @rb.setter
    def rb(self, rb):
        """
        Set the rb number.
        """
        self._rb = rb

    @property
    def wr(self):
        """
        Get the wr number.
        """
        return self._wr
    
    @wr.setter
    def wr(self, wr):
        """
        Set the wr number.
        """
        self._wr = wr

    @property
    def te(self):
        """
        Get the te number.
        """
        return self._te
    
    @te.setter
    def te(self, te):
        """
        Set the te number.
        """
        self._te = te

    @property
    def k(self):
        """
        Get the k number.
        """
        return self._k
    
    @k.setter
    def k(self, k):
        """
        Set the k number.
        """
        self._k = k

    def get_total_players(self):
        """
        Get the total number of players allowed
        :return: The total number of players allowed
        """
        return self.qb + self.rb + self.wr + self.te + self.k + self.bench

    def __str__(self):
        """
        Get the string representation of the constraints
        :return: The string representation of the constraints
        """
        return f"QB: {self.qb}, RB: {self.rb}, WR: {self.wr}, TE: {self.te}, K: {self.k}, Bench: {self.bench}"

    @staticmethod
    def from_constraints_response(constraints_response):
        """
        Forms new LeagueConstraint object from constraints response string.
        :param constraints_response: The constraints response string.
        :return: The new LeagueConstraint object.
        """
        league_constraints = {}
        constraints = constraints_response.split(",")
        for part in constraints:
            key, value = part.split("-")
            league_constraints[key] = int(value)
        return LeagueConstraint(
            league_constraints["QB"],
            league_constraints["RB"],
            league_constraints["WR"],
            league_constraints["TE"],
            league_constraints["K"],
            league_constraints["BENCH"]
        )