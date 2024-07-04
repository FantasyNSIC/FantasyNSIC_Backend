UPDATE team_roster
SET status = 'bench'
WHERE player_id = %s
AND user_team_id = %s