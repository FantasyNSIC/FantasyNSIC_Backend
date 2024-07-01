SELECT stW1.*, points.week_1, stW2.*, points.week_2, stW3.*, points.week_3
FROM player_stats_week_1 stW1
JOIN player_points_scored points ON points.player_id = stW1.player_id
JOIN player_stats_week_2 stW2 ON stW2.player_id = stW1.player_id
JOIN player_stats_week_3 stW3 ON stW3.player_id = stW1.player_id
WHERE stW1.player_id = %s