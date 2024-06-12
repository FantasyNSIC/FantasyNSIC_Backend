SELECT user_team.*, users.full_name
FROM user_team
JOIN users ON user_team.user_id = users.user_id
WHERE user_team.league_id = %s