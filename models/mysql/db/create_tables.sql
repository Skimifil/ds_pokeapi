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
    name VARCHAR(255),
    effect MEDIUMTEXT,
    pokemon_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id)
);

CREATE TABLE moves (
    move_id INT PRIMARY KEY,
    name VARCHAR(255),
    effect MEDIUMTEXT,
    pokemon_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id)
);

CREATE TABLE status (
    name VARCHAR(255),
    base_stats INT,
    pokemon_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id)
);