SELECT ut.team_name, u.full_name, tr.*, ups.{current_week}
FROM user_team ut
JOIN users u ON u.user_id = ut.user_id
JOIN team_records tr ON tr.user_team_id = ut.user_team_id
JOIN user_points_scored ups ON ups.user_team_id = ut.user_team_id
WHERE ut.user_team_id = %s
OR ut.user_team_id IN (
    SELECT utm.{current_week}
    FROM user_team_matchups utm
    WHERE utm.user_team_id = %s
)