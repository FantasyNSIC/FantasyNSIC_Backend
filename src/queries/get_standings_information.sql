SELECT team_records.*, user_team.team_name
FROM team_records
JOIN user_team ON team_records.user_team_id = user_team.user_team_id
WHERE user_team.league_id = %s