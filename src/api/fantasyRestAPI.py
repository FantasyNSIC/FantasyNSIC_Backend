""" File containing the REST API for the fantasy football application """

from datetime import timedelta
from flask import Flask, request, session
from flask_cors import CORS
from flask_session import Session
from ..util.logger import Logger
from ..service.authService import *
from ..service.getDBService import *
from ..service.postDBService import *

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['http://localhost:8080'])
logger = Logger()

app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=2)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_COOKIE_NAME"] = "nsic_fantasy_session"
app.config["SESSION_COOKIE_SAMESITE"] = 'Lax'
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SECURE"] = False
Session(app)

@app.route('/auth/login', methods=['POST'])
def login():
    # Login a user.
    username = request.json['username']
    password = request.json['password']
    authenticated = authenticate_user(username, password)
    if authenticated[0]:
        session.clear()
        session['username'] = username
        session['user_id'] = authenticated[1]
        return {'status': True,
                'message': 'Logged in successfully.',
                'user_id': authenticated[1],
                'user_teams': authenticated[2][1]
        }
    else:
        return {'status': False, 'message': 'Invalid credentials.'}

@app.route('/auth/logout', methods=['POST'])
def logout():
    # Logout a user.
    session.clear()
    return {'message': 'User succesfully logged out.'}

@app.route('/auth/verifyUser', methods=['GET'])
def verify_user():
    # Verify a user.
    if not session.get('username') or not session.get('user_id'):
        return {'status': False, 'message': 'User is not logged in.'}
    return {'status': True, 'message': 'User is logged in.'}

@app.route('/db/getMyTeamInfo', methods=['GET'])
def get_team_roster():
    # Fetch user-team info and roster from the database.
    user_team_id = request.args.get('user_team_id')
    return my_team_information_service(user_team_id).toJson()

@app.route('/db/getAvailablePlayers', methods=['GET'])
def get_available_players():
    # Fetch available players from the database.
    league_id = int(request.args.get('league_id'))
    return available_players_service(league_id).toJson()

@app.route('/db/getMatchupInfo', methods=['GET'])
def get_matchup_info():
    # Fetch team information from the database.
    user_team_id = request.args.get('user_team_id')
    return matchup_information_service(user_team_id).toJson()

@app.route('/db/getScoreboardInfo', methods=['GET'])
def get_scoreboard_info():
    # Fetch league information from the database.
    league_id = request.args.get('league_id')
    return scorboard_information_service(league_id).toJson()

@app.route('/db/getLeagueInfo', methods=['GET'])
def get_league_info():
    # Fetch league information from the database.
    league_id = request.args.get('league_id')
    return league_information_service(league_id).toJson()

@app.route('/db/getStandingsInfo', methods=['GET'])
def get_standings_info():
    # Fetch standings information from the database.
    league_id = request.args.get('league_id')
    return standings_information_service(league_id).toJson()

@app.route('/db/getNSICPlayerInfo', methods=['POST'])
def get_nsic_player_info():
    # Fetch player information from the database.
    player_id = request.json['player_id']
    return get_nsic_player_service(player_id).toJson()

@app.route('/rq/addNSICPlayerToRoster', methods=['POST'])
def add_nsic_player_to_roster():
    # Add a NSIC player to a user's roster.
    player_id = request.json['player_id']
    user_team_id = request.json['user_team_id']
    league_id = request.json['league_id']
    return add_nsic_player_to_roster_service(player_id, user_team_id, league_id).toJson()

@app.route('/rq/dropNSICPlayerFromRoster', methods=['POST'])
def drop_nsic_player_from_roster():
    # Drop a NSIC player from a user's roster.
    player_id = request.json['player_id']
    user_team_id = request.json['user_team_id']
    league_id = request.json['league_id']
    return drop_nsic_player_from_roster_service(player_id, user_team_id, league_id).toJson()

@app.route('/rq/moveNSICPlayersOnRoster', methods=['POST'])
def move_nsic_players_on_roster():
    # Move NSIC players on a user's roster.
    user_team_id = request.json['user_team_id']
    league_id = request.json['league_id']
    player_id_1 = request.json['player_id_1']
    player_id_2 = request.json['player_id_2']
    return move_nsic_players_on_roster_service(user_team_id, league_id, player_id_1, player_id_2).toJson()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
