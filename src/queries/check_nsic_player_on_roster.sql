SELECT tr.*, ut.user_team_id, l.league_id
FROM team_roster tr
JOIN user_team ut ON tr.user_team_id = ut.user_team_id
JOIN leagues l ON ut.league_id = l.league_id
WHERE tr.user_team_id = %s
AND tr.player_id = %s
AND l.league_id = %s