SELECT ut.user_team_id, ut.league_id
FROM user_team ut
WHERE ut.user_id = %s