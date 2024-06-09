SELECT team_roster.status, nsic_players.*
FROM team_roster
JOIN nsic_players ON team_roster.player_id = nsic_players.player_id
WHERE team_roster.user_team_id = %s