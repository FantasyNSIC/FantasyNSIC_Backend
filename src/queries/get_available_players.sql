SELECT * 
FROM nsic_players np
WHERE NOT EXISTS (
    SELECT 1 
    FROM taken_players tp
    WHERE tp.player_id = np.player_id 
    AND tp.league_id = %s
)