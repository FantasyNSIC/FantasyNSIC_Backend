""" File containing the REST API for the fantasy football application """

from datetime import timedelta
from flask import Flask, request, session
from flask_cors import CORS
from flask_session import Session
from flask_socketio import SocketIO, emit
from ..util.logger import Logger
from ..service.authService import *
from ..service.getDBService import *
from ..service.postDBService import *

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['https://localhost:8080'])
logger = Logger()

app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=2)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_COOKIE_NAME"] = "nsic_fantasy_session"
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SECURE"] = True
Session(app)

socketio = SocketIO(app, cors_allowed_origins="*")

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
        session['user_teams'] = authenticated[2]
        return {'status': True,
                'message': 'Logged in successfully.',
                'user_id': authenticated[1],
                'user_teams': authenticated[2]
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
    if not session.get('username') or not session.get('user_id') or not session.get('user_teams'):
        return {'status': False, 'message': 'User is not logged in.'}
    return {'status': True, 'message': 'User is logged in.', 'user_teams': session.get('user_teams')}

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

@app.route('/db/getDraftBoardInfo', methods=['GET'])
def get_draft_board_info():
    # Fetch draft board information from the database.
    league_id = request.args.get('league_id')
    user_team_id = request.args.get('user_team_id')
    return draft_board_information_service(league_id, user_team_id).toJson()

@app.route('/db/getWaiverWireClaims', methods=['GET'])
def get_waiver_wire_claims():
    # Fetch waiver wire claims from the database.
    user_team_id = request.args.get('user_team_id')
    league_id = request.args.get('league_id')
    return waiver_wire_claims_service(user_team_id, league_id).toJson()

@app.route('/db/getNSICPlayerInfo', methods=['POST'])
def get_nsic_player_info():
    # Fetch player information from the database.
    player_id = request.json['player_id']
    return get_nsic_player_service(player_id).toJson()

@app.route('/db/getUserTeamRoster', methods=['POST'])
def get_user_team_roster():
    # Fetch user team roster from the database.
    league_id = request.json['league_id']
    user_team_id = request.json['user_team_id']
    return get_user_team_roster_service(league_id, user_team_id).to_json()

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

@app.route('/rq/draftNSICPlayerToRoster', methods=['POST'])
def draft_nsic_player_to_roster():
    # Draft a NSIC player to a user's roster.
    player_id = request.json['player_id']
    draft_pick = request.json['draft_pick']
    user_team_id = request.json['user_team_id']
    league_id = request.json['league_id']
    return draft_nsic_player_to_roster_service(player_id, draft_pick, user_team_id, league_id).toJson()

@app.route('/rq/submitWaiverWireClaim', methods=['POST'])
def submit_waiver_wire_claim():
    # Submit a waiver wire claim.
    user_team_id = request.json['user_team_id']
    league_id = request.json['league_id']
    player_add = request.json['player_add']
    player_remove = request.json['player_remove']
    return submit_waiver_wire_claim_service(user_team_id, league_id, player_add, player_remove).toJson()

@app.route('/rq/deleteWaiverWireClaim', methods=['POST'])
def delete_waiver_wire_claim():
    # Delete a waiver wire claim.
    user_team_id = request.json['user_team_id']
    league_id = request.json['league_id']
    player_add = request.json['player_add']
    player_remove = request.json['player_remove']
    return delete_waiver_wire_claim_service(user_team_id, league_id, player_add, player_remove).toJson()

@socketio.on('connect')
def handle_connect():
    logger.info('Client connected to the server.')

@socketio.on('disconnect')
def handle_disconnect():
    logger.info('Client disconnected from the server.')
    emit('disconnect')

@socketio.on('draft_submit')
def handle_message(data):
    logger.info('Pick received: ' + str(data))
    emit('draft_update')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True, ssl_context=('/certB.pem', '/keyB.pem'))
