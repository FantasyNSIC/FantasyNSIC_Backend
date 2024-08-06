SELECT *
FROM draft_order
WHERE draft_pick = %s
AND league_id = %s
AND user_team_id = %s