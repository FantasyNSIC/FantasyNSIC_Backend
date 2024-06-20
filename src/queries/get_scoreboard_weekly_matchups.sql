SELECT utm.user_team_id, utm.{current_week}, ut.*, ups.{current_week}, tr.wins, tr.losses
FROM user_team_matchups utm
JOIN user_team ut ON utm.user_team_id = ut.user_team_id
JOIN user_points_scored ups ON utm.user_team_id = ups.user_team_id
JOIN team_records tr ON utm.user_team_id = tr.user_team_id
WHERE utm.league_id = %s