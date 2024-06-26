""" File containing the REST API for the fantasy football application """

import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from ..util.logger import Logger
from ..service.getDBService import *
from ..service.postDBService import *

app = Flask(__name__)
CORS(app)
logger = Logger()

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
