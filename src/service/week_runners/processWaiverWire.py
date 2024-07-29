"""This file will handle all the waiver wire processing for the week, it is to be ran only once a week."""

from ...util.connection import connect_to_fantasyDB
from ..postDBService import add_nsic_player_to_roster_service, drop_nsic_player_from_roster_service
import time

def process_waiver_wire(league_id: int):
    """
    Main function for carrying out waiver wire processing for the week.
    :param league_id: The league ID of the league to process the waiver wire for.
    """
    # Connect to the database.
    connection = connect_to_fantasyDB()
    cursor = connection.cursor()

    try:
        # Get the waiver wire order for the league.
        cursor.execute("""
            SELECT waiver_order
            FROM waiver_wire_priority
            WHERE league_id = %s
            """, (league_id,))
        waiver_order = cursor.fetchone()[0]
        ordered_user_teams = [team['user_team_id'] for team in waiver_order]

        # Get the waiver wire claims for the league.
        cursor.execute("""
            SELECT user_team_id, player_add, player_remove
            FROM waiver_wire_claim
            WHERE league_id = %s
            """, (league_id,))
        waiver_claims = cursor.fetchall()

        # Format claims based on fequency of claim.
        claims = {}
        for claim in waiver_claims:
            if claim[1] not in claims:
                claims[claim[1]] = []
            claims[claim[1]].append(claim)

        # Sort the dictionary by the number of values for each key
        sorted_claims = sorted(claims.items(), key=lambda item: len(item[1]), reverse=True)

        # Process the waiver wire claims, making sure to
        # process claim based on user_team priority
        break_flag = False
        for claim in sorted_claims:
            print(f"Processing waiver wire claim for player: {claim[0]}")
            break_flag = False
            for team in ordered_user_teams:
                for c in claim[1]:
                    if c[0] == team:
                        pc = process_claim(c, league_id)
                        if pc:
                            # Move 1st priority team to the end of the list
                            ordered_user_teams.remove(team)
                            ordered_user_teams.append(team)
                            break_flag = True
                            break
                if break_flag:
                    break

        # Clear the waiver wire claims table.
        cursor.execute("""
            DELETE FROM waiver_wire_claim
            WHERE league_id = %s
            """, (league_id,))

        connection.commit()

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

def process_claim(claim, league_id):
    """
    Attempts to process a single waiver wire claim.
    :param claim: The waiver wire claim to process.
    :param league_id: The league ID of the league to process the claim for.
    """
    if claim[2] is not None:
        time.sleep(2)
        drop_response = drop_nsic_player_from_roster_service(claim[2], claim[0], league_id)
        if not drop_response.success:
            print(f"user_team: {claim[0]} - {drop_response.message}")
            return False
    time.sleep(2)
    add_response = add_nsic_player_to_roster_service(claim[1], claim[0], league_id)
    if not add_response.success:
        print(f"user_team: {claim[0]} - {add_response.message}")
        # If the add fails, add the dropped player back to the roster.
        if claim[2] is not None:
            time.sleep(2)
            add_response = add_nsic_player_to_roster_service(claim[2], claim[0], league_id)
            print(f"user_team: {claim[0]} - {add_response.message} (added back dropped player)")
        return False
    print(f"Successfully processed waiver wire claim for user_team_id: {claim[0]} player: {claim[1]}")
    return True

if __name__ == '__main__':
    process_waiver_wire(00000)
