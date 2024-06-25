SELECT stW1.*, points.week_1
FROM player_stats_week_1 stW1
JOIN player_points_scored points ON points.player_id = stW1.player_id
WHERE stW1.player_id = %s