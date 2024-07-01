DELETE FROM taken_players
WHERE league_id = %s
AND user_team_id = %s
AND player_id = %s
