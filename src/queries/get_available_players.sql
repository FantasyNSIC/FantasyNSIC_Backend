SELECT np.*, pps.total_points
FROM nsic_players np
JOIN player_points_scored pps ON np.player_id = pps.player_id
WHERE NOT EXISTS (
    SELECT 1 
    FROM taken_players tp
    WHERE tp.player_id = np.player_id 
    AND tp.league_id = %s
)