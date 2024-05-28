""" File containing the REST API for the fantasy football application """

import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.util.logger import Logger

app = Flask(__name__)
CORS(app)
logger = Logger()

@app.route('/db/getUserTeam', methods=['GET'])
def get_team_info():
    # Fetch team information from the database.
    team_id = request.args.get('team_id')
    return jsonify(team_id)

@app.route('/db/getLeagueInfo', methods=['GET'])
def get_league_info():
    # Fetch league information from the database.
    league_id = request.args.get('league_id')
    return jsonify(league_id)

@app.route('/db/getTeamRoster', methods=['GET'])
def get_team_roster():
    # Fetch team roster from the database.
    team_id = request.args.get('team_id')
    return jsonify(team_id)

@app.route('/db/getPlayerInfo', methods=['POST'])
def get_player_info():
    # Fetch player information from the database.
    player_id = request.json['player_id']
    return jsonify(player_id)
