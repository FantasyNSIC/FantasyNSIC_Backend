SELECT dr.draft_pick, dr.league_id, dr.user_team_id, np.*
FROM draft_order dr
LEFT JOIN nsic_players np ON dr.player_id = np.player_id
WHERE dr.league_id = %s