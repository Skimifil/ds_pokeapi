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

DELIMITER //

CREATE PROCEDURE add_pokemon_move(IN pokemon_id INT, IN move_id INT)
BEGIN
    -- Verificar se Pokémon e movimento existem antes de inserir na tabela de relacionamentos
    IF EXISTS (SELECT 1 FROM pokemon WHERE pokemon_id = pokemon_id) AND
       EXISTS (SELECT 1 FROM moves WHERE move_id = move_id) THEN
        INSERT INTO pokemon_moves (pokemon_id, move_id)
        VALUES (pokemon_id, move_id);
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid pokemon_id or move_id';
    END IF;
END //

DELIMITER ;
