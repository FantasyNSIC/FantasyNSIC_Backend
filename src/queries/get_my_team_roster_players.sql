SELECT team_roster.status, nsic_players.*, player_points_scored.total_points
FROM team_roster
JOIN nsic_players ON team_roster.player_id = nsic_players.player_id
JOIN player_points_scored ON team_roster.player_id = player_points_scored.player_id
WHERE team_roster.user_team_id = %s