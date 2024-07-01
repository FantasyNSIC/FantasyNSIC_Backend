"""Handles creating a new UserRoster for the myTeamInfo service based on league constraints."""
from ..classes.User_Roster import UserRoster
from ..classes.NSIC_Player import NSIC_Player
from ..classes.LeagueConstraint import LeagueConstraint

def handle_roster_creation(res_roster: list, constraints: str):
    """
    Handles creating a new UserRoster for the myTeamInfo service based on league constraints.
    :param res_roster: The roster information from the database.
    :param constraints: The league constraints.
    :return: A new UserRoster object.
    """
    new_roster = UserRoster()
    new_constraints = LeagueConstraint.from_constraints_response(constraints)
    overflowFlag = ""
    for player in res_roster:
        new_player = NSIC_Player.from_tuple(player[1:])
        if player[0] == 'active':
            new_roster.add_player(new_player, new_player.pos)
        elif player[0] == 'bench':
            new_roster.add_player(new_player, 'BENCH')
    QB_roster = compare_constraint_with_pos(new_roster.QB, new_constraints.qb)
    new_roster.QB = QB_roster[0]
    if QB_roster[1]:
        overflowFlag = "QB"
    RB_roster = compare_constraint_with_pos(new_roster.RB, new_constraints.rb)
    new_roster.RB = RB_roster[0]
    if RB_roster[1]:
        overflowFlag = "RB"
    WR_roster = compare_constraint_with_pos(new_roster.WR, new_constraints.wr)
    new_roster.WR = WR_roster[0]
    if WR_roster[1]:
        overflowFlag = "WR"
    TE_roster = compare_constraint_with_pos(new_roster.TE, new_constraints.te)
    new_roster.TE = TE_roster[0]
    if TE_roster[1]:
        overflowFlag = "TE"
    K_roster = compare_constraint_with_pos(new_roster.K, new_constraints.k)
    new_roster.K = K_roster[0]
    if K_roster[1]:
        overflowFlag = "K"
    BENCH_roster = compare_constraint_with_bench(new_roster.BENCH, new_constraints.bench, new_constraints.get_total_players())
    new_roster.BENCH = BENCH_roster[0]
    if BENCH_roster[1]:
        overflowFlag = "BENCH"
    return new_roster, overflowFlag

def compare_constraint_with_pos(pos_roster, pos_constraint):
    """
    Compares the number of pos in the roster with the respective constraint.
    :param pos_roster: The roster of pos.
    :param pos_constraint: The number of pos allowed.
    :return: List of pos to be replaced into new_roster.
    """
    pos_redner_list = []
    if len(pos_roster) == pos_constraint:
        return pos_roster, False
    elif len(pos_roster) < pos_constraint:
        for i in range(pos_constraint - len(pos_roster)):
            pos_redner_list.append(NSIC_Player.empty_player())
        return pos_roster + pos_redner_list, False
    elif len(pos_roster) > pos_constraint:
        return pos_roster[:pos_constraint], True
    
def compare_constraint_with_bench(bench_roster, bench_constraint, total_players):
    """
    Compares the number of bench players in the roster with the respective constraint.
    :param bench_roster: The roster of bench players.
    :param bench_constraint: The number of bench players allowed.
    :return: List of bench players to be replaced into new_roster.
    """
    bench_render_list = []
    if (len(bench_roster) == bench_constraint) or (len(bench_roster) > bench_constraint and len(bench_roster) <= total_players):
        return bench_roster, False
    elif len(bench_roster) < bench_constraint:
        for i in range(bench_constraint - len(bench_roster)):
            bench_render_list.append(NSIC_Player.empty_player())
        return bench_roster + bench_render_list, False
    elif len(bench_roster) > bench_constraint and len(bench_roster) > total_players:
        return bench_roster[:total_players], True
