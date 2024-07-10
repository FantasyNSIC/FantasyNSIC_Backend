SELECT ut.user_team_id, ut.team_name, ut.league_id, l.league_name
FROM user_team ut
JOIN leagues l ON ut.league_id = l.league_id
WHERE ut.user_id = %s