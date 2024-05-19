GRANT ALL PRIVILEGES ON db_pokeapi.* TO 'myuser'@'%';
FLUSH PRIVILEGES;

USE db_pokeapi;

CREATE TABLE pokemon (
    pokemon_id INT PRIMARY KEY,
    name VARCHAR(255),
    height INT,
    weight INT
);

CREATE TABLE abilities (
    abilitie_id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE moves (
    move_id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE pokemon_abilities (
    pokemon_id INT,
    ability_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
    FOREIGN KEY (ability_id) REFERENCES abilities(abilitie_id)
);

CREATE TABLE pokemon_moves (
    pokemon_id INT,
    move_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
    FOREIGN KEY (move_id) REFERENCES moves(move_id)
);
