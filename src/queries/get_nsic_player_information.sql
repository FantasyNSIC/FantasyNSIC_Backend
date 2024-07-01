SELECT nsp.*, pps.total_points, nst.*
FROM nsic_players nsp
JOIN player_points_scored pps ON pps.player_id = nsp.player_id
JOIN nsic_teams nst ON nst.team_id = nsp.team_id
WHERE nsp.player_id = %s