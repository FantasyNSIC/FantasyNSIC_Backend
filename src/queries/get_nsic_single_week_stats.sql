SELECT psw.*, pps.{week}
FROM player_stats_{week} psw
JOIN player_points_scored pps ON psw.player_id = pps.player_id
WHERE psw.player_id = %s