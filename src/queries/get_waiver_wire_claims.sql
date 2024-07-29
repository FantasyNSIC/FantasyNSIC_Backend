SELECT 
    add_player.player_id, 
        add_player.first_name, 
        add_player.last_name, 
        add_player.team_id, 
        add_player.pos, 
        add_player.cls, 
        add_player.jersey_number, 
        add_player.height, 
        add_player.weight, 
        remove_player.player_id, 
        remove_player.first_name, 
        remove_player.last_name, 
        remove_player.team_id, 
        remove_player.pos, 
        remove_player.cls, 
        remove_player.jersey_number, 
        remove_player.height, 
        remove_player.weight
FROM waiver_wire_claim wwc
JOIN nsic_players add_player ON wwc.player_add = add_player.player_id
LEFT JOIN nsic_players remove_player ON wwc.player_remove = remove_player.player_id
WHERE wwc.user_team_id = %s
AND wwc.league_id = %s