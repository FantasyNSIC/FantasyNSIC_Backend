SELECT l.league_constraint, ut.team_name, l.league_name, u.full_name, tr.wins, tr.losses
FROM user_team ut
JOIN leagues l ON ut.league_id = l.league_id
JOIN users u ON ut.user_id = u.user_id
JOIN team_records tr ON ut.user_team_id = tr.user_team_id
WHERE ut.user_team_id = %s