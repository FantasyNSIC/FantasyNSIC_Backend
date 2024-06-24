SELECT l.current_week, l.league_constraint
FROM user_team ut
JOIN leagues l ON l.league_id = ut.league_id
WHERE ut.user_team_id = %s