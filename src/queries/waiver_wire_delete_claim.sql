DELETE FROM waiver_wire_claim
WHERE league_id = %s
AND user_team_id = %s
AND player_add = %s
AND player_remove = %s