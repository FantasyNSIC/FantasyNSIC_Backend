"""Handles determining whether or not there is space on a roster for a player to be added."""
from ..classes.User_Roster import UserRoster
from ..classes.NSIC_Player import NSIC_Player
from ..classes.LeagueConstraint import LeagueConstraint

def handle_new_player_to_roster_determination(res_roster: list, constraints: str, new_pos: str):
    """
    Handles forming a new UserRoster and then checking if a new player can be
    Added based on that new player's position.
    :param res_roster: The roster information from the database.
    :param constraints: The league constraints.
    :param new_pos: The position of the new player.
    :return: A boolean indicating if the player can be added to the roster, and where to add player.
    """
    new_roster = UserRoster()
    new_constraints = LeagueConstraint.from_constraints_response(constraints)
    for player in res_roster:
        new_player = NSIC_Player.from_tuple(player[1:])
        if player[0] == 'active':
            new_roster.add_player(new_player, new_player.pos)
        elif player[0] == 'bench':
            new_roster.add_player(new_player, 'BENCH')
    # Check active spots first
    if new_pos == 'QB':
        check = check_pos_spots(new_roster.QB, new_constraints.qb)
        if check:
            return True, 'active'
    elif new_pos == 'RB':
        check = check_pos_spots(new_roster.RB, new_constraints.rb)
        if check:
            return True, 'active'
    elif new_pos == 'WR':
        check = check_pos_spots(new_roster.WR, new_constraints.wr)
        if check:
            return True, 'active'
    elif new_pos == 'TE':
        check = check_pos_spots(new_roster.TE, new_constraints.te)
        if check:
            return True, 'active'
    elif new_pos == 'K':
        check = check_pos_spots(new_roster.K, new_constraints.k)
        if check:
            return True, 'active'
    # Check bench spots if active spots are full
    check = check_pos_spots(new_roster.BENCH, new_constraints.bench)
    if check:
        return True, 'bench'
    return False, ''
    
def check_pos_spots(pos_roster, pos_constraint):
    """
    Compares the number of pos in the roster with the respective constraint.
    :param pos_roster: The roster of pos.
    :param pos_constraint: The number of pos allowed.
    :return: boolean indicating if the player can be added to the roster.
    """
    if len(pos_roster) < pos_constraint:
        return True
    return False
