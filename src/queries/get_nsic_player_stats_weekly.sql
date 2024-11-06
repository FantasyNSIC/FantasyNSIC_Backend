SELECT stW1.*, points.week_1, stW2.*, points.week_2, stW3.*, points.week_3, stW4.*, points.week_4, stW5.*, points.week_5, stW6.*, points.week_6, stW7.*, points.week_7, stW8.*, points.week_8, stW9.*, points.week_9, stW10.*, points.week_10, stW11.*, points.week_11, stW12.*, points.week_12
FROM player_stats_week_1 stW1
JOIN player_points_scored points ON points.player_id = stW1.player_id
JOIN player_stats_week_2 stW2 ON stW2.player_id = stW1.player_id
JOIN player_stats_week_3 stW3 ON stW3.player_id = stW1.player_id
JOIN player_stats_week_4 stW4 ON stW4.player_id = stW1.player_id
JOIN player_stats_week_5 stW5 ON stW5.player_id = stW1.player_id
JOIN player_stats_week_6 stW6 ON stW6.player_id = stW1.player_id
JOIN player_stats_week_7 stW7 ON stW7.player_id = stW1.player_id
JOIN player_stats_week_8 stW8 ON stW8.player_id = stW1.player_id
JOIN player_stats_week_9 stW9 ON stW9.player_id = stW1.player_id
JOIN player_stats_week_10 stW10 ON stW10.player_id = stW1.player_id
JOIN player_stats_week_11 stW11 ON stW11.player_id = stW1.player_id
JOIN player_stats_week_12 stW12 ON stW12.player_id = stW1.player_id
WHERE stW1.player_id = %s