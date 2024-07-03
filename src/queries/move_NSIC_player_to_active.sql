UPDATE team_roster
SET status = 'active'
WHERE player_id = %s
AND user_team_id = %s