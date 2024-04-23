### Projeto

# Pokeapi - CoderHouse
Coleta os dados da API [PokeAPI](https://pokeapi.co/) para tratamento, armazenamento e manipulação.


## Fluxo
1. Conecta na API
2. Através dos endpoints, coleta as informações dos Pokemons, sendo:
   - Pokemon
   - Habilidades
   - Sons
   - Formas
   - Indice dos jogos
   - Movimentos
   - Espécie
   - Sprites
   - Status
   - Tipos
3. Armazena em um banco de dados
4. Através de um Notebook Jupyter, faz a analise dos dados


## Pré-reqs
É preciso ter uma banco de dados MySQL para armazenamento dos dados. Criei um 'docker-compose.yml' para subir um MySQL no Docker pra facilitar o trabalho em teste e homologação.

Com o banco funcional, crie o arquivo 'config.py' dentro da pasta 'src/' e adicione o trecho abaixo no arquivo (caso queira trocar os dados de acesso, lembre-se de avaliar o 'docker-compose.yml' também).

```shell
MYSQL_CONFIG = {
    'MYSQLUSER': 'myuser',
    'MYSQLPASSWORD': 'mypassword',
    'MYSQLSERVER': '172.19.0.2',
    'MYSQLDB': 'db_pokeapi',
}
```

## Infraestrutura do Banco de Dados Pokémon

```mermaid
erDiagram
    abilities {
        INT ability_id PK
        VARCHAR name
        MEDIUMTEXT effect
    }
    
    pokemon {
        INT pokemon_id PK
        VARCHAR name
        INT height
        INT weight
    }

    moves {
        INT move_id PK
        VARCHAR name
        MEDIUMTEXT effect
    }

    pokemon_abilities {
        INT pokemon_id FK
        INT ability_id FK
    }

    pokemon_moves {
        INT pokemon_id FK
        INT move_id FK
    }

    pokemon ||--o{ pokemon_abilities : "has"
    pokemon ||--o{ pokemon_moves : "has"
    abilities ||--o{ pokemon_abilities : "has"
    moves ||--o{ pokemon_moves : "has"
```
## Endpoints de referência na API
[Pokemons](https://pokeapi.co/api/v2/pokemon/)
