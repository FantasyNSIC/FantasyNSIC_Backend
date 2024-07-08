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
            return check_password_hash(res[0], password), res[1]
    except Exception as e:
        print(e)
        return False, None
    finally:
        cur.close()
        conn.close()
    return False, None
