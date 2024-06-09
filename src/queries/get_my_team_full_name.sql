SELECT full_name
FROM users
WHERE EXISTS (
    SELECT 1
    FROM user_team
    WHERE user_team.user_id = users.user_id
    AND user_team.user_team_id = %s
)