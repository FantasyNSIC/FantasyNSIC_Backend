SELECT league_name, league_constraint, draft_enable
FROM leagues
JOIN draft_properties ON leagues.league_id = draft_properties.league_id
WHERE leagues.league_id = %s