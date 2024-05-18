MYSQL_CONFIG = {
    'MYSQLUSER': 'myuser',
    'MYSQLPASSWORD': 'mypassword',
    'MYSQLSERVER': '172.15.0.2',
    'MYSQLDB': 'db_pokeapi',
}

QUERY_INSERT = {
    'pokemon': 'INSERT INTO pokemon (pokemon_id, name, height, weight) VALUES (%(pokemon_id)s, %(name)s, %(height)s, %(weight)s)',
    'abilities': 'INSERT INTO abilities (abilitie_id, name) VALUES (%(abilitie_id)s, %(name)s)',
    'moves': 'INSERT INTO moves (move_id, name) VALUES (%(move_id)s, %(name)s)',
    'pokemon_abilities': 'INSERT INTO pokemon_abilities (pokemon_id, ability_id) VALUES (%(pokemon_id)s, %(ability_id)s)',
    'pokemon_moves': 'INSERT INTO pokemon_moves (pokemon_id, move_id) VALUES (%(pokemon_id)s, %(move_id)s)'
}