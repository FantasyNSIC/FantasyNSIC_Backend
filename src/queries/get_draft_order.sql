SELECT dr.draft_pick, dr.league_id, dr.user_team_id, ut.team_name, np.*
FROM draft_order dr
JOIN user_team ut ON dr.user_team_id = ut.user_team_id
LEFT JOIN nsic_players np ON dr.player_id = np.player_id
WHERE dr.league_id = %s