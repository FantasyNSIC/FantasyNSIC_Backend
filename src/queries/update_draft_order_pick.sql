UPDATE draft_order
SET
    player_id = %s
WHERE
    draft_pick = %s
    AND league_id = %s
    AND user_team_id = %s;