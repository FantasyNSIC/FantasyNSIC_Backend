"""Service file for all authentication-related functions."""

from ..util.connection import connect_to_fantasyDB
from werkzeug.security import check_password_hash

def authenticate_user(username, password):
    """
    Authenticates a user with the given username and password.
    :param username: The username of the user.
    :param password: The password of the user.
    :return: True if the user is authenticated, False otherwise.
    """
    conn = connect_to_fantasyDB()
    cur = conn.cursor()
    try:
        with open('src/queries/get_user_credentials.sql', 'r') as sql:
            query = sql.read()
        cur.execute(query, (username,))
        res = cur.fetchone()
        if res is not None:
            with open('src/queries/auth_get_user_teams.sql', 'r') as sql:
                query = sql.read()
            cur.execute(query, (res[1],))
            res_teams = cur.fetchall()
            teams = [{'user_team_id': team[0], 'league_id': team[1]} for team in res_teams]
            return check_password_hash(res[0], password), res[1], teams
    except Exception as e:
        print(e)
        return False, None, []
    finally:
        cur.close()
        conn.close()
    return False, None, []
