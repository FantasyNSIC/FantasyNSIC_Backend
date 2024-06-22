"""Handle creating a new roster given the tuple response and the matching user_team_id."""
from ..classes.User_Roster import UserRoster
from ..classes.NSIC_Player import NSIC_Player
from ..classes.LeagueConstraint import LeagueConstraint

def matchup_roster_creation(res_roster: list, user_team_id: int, constraints: str):
    """
    Handles creating a new UserRoster for the matchup information service.
    :param res_roster: The roster information from the database.
    :param user_team_id: The ID of the user's team.
    :param constraints: The league constraints.
    :return: A new UserRoster object.
    """
    new_roster = UserRoster()
    new_constraints = LeagueConstraint.from_constraints_response(constraints)
    filtered_roster = [player for player in res_roster if player[0] == user_team_id]
    for player in filtered_roster:
        new_player = NSIC_Player.from_tuple(player[2:])
        if player[1] == 'active':
            new_roster.add_player(new_player, new_player.pos)
        elif player[1] == 'bench':
            new_roster.add_player(new_player, 'BENCH')
    new_roster.QB = compare_constraint_with_pos(new_roster.QB, new_constraints.qb)
    new_roster.RB = compare_constraint_with_pos(new_roster.RB, new_constraints.rb)
    new_roster.WR = compare_constraint_with_pos(new_roster.WR, new_constraints.wr)
    new_roster.TE = compare_constraint_with_pos(new_roster.TE, new_constraints.te)
    new_roster.K = compare_constraint_with_pos(new_roster.K, new_constraints.k)
    new_roster.BENCH = compare_constraint_with_bench(new_roster.BENCH, new_constraints.bench, new_constraints.get_total_players())
    return new_roster

def compare_constraint_with_pos(pos_roster, pos_constraint):
    """
    Compares the number of pos in the roster with the respective constraint.
    :param pos_roster: The roster of pos.
    :param pos_constraint: The number of pos allowed.
    :return: List of pos to be replaced into new_roster.
    """
    pos_redner_list = []
    if len(pos_roster) == pos_constraint:
        return pos_roster
    elif len(pos_roster) < pos_constraint:
        for i in range(pos_constraint - len(pos_roster)):
            pos_redner_list.append(NSIC_Player.empty_player())
        return pos_roster + pos_redner_list
    elif len(pos_roster) > pos_constraint:
        return pos_roster[:pos_constraint]
    
def compare_constraint_with_bench(bench_roster, bench_constraint, total_players):
    """
    Compares the number of bench players in the roster with the respective constraint.
    :param bench_roster: The roster of bench players.
    :param bench_constraint: The number of bench players allowed.
    :return: List of bench players to be replaced into new_roster.
    """
    bench_render_list = []
    if (len(bench_roster) == bench_constraint) or (len(bench_roster) > bench_constraint and len(bench_roster) <= total_players):
        return bench_roster
    elif len(bench_roster) < bench_constraint:
        for i in range(bench_constraint - len(bench_roster)):
            bench_render_list.append(NSIC_Player.empty_player())
        return bench_roster + bench_render_list
    elif len(bench_roster) > bench_constraint and len(bench_roster) > total_players:
        return bench_roster[:total_players]
