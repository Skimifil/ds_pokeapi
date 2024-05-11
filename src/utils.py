from src.logger import *
from src.connect_api import connect_api
from src.connect_database import *
from src.config import QUERY_INSERT


logger_app_functions = configurar_logger("app_functions", "app_functions.log")


def get_id_from_url(url):
    """
    Get the id in the URL pass in the parameter.
    :param url: (str) The url to get the id from.
    :return: The ID of the url passed in.

    Exemple: get_id_from_url(https://url.com.br)
    """
    return int(url.split('/')[-2])


def get_all_pokemons_from_api():
    """
    Get all pokemons from API.
    :return: A list of all pokemons.
    Exemple: get_all_pokemons_from_api()
    """
    try:
        data = connect_api(f'https://pokeapi.co/api/v2/pokemon/?limit=2')
        return data[0]['url']
    except Exception as e:
        alerta(e)


def get_pokemon_info(endpoint_poki):
    """
    Get pokemon info.
    :param endpoint_poki: (str) URL of the pokemon infos.
    :return: All the information of the pokemons.
    Exemple: get_pokemon_info('https://pokeapi.co/api/v2/pokemon/1')
    """
    try:

        data = connect_api(endpoint_poki)

        podemon_id = int(endpoint_poki.split('/')[-2])
        pokemon_name = data['name']
        pokemon_height = data['height']
        pokemon_weight = data['weight']

        results = [{
            'pokemon_id': podemon_id,
            'name': pokemon_name,
            'height': pokemon_height,
            'weight': pokemon_weight
        }]

        logger_app_functions.info(f'[get_pokemon_info] Create a JSON with the information about the Pokemons: {results}')

        return results
    except Exception as e:
        logger_app_functions.error(f'[get_pokemon_info] An error has occurred: {e} ')
        alerta(e)


def get_abilities_from_api(endpoint_pok):
    """
    Get abilities of the pokemons.
    :param endpoint_pok: (str) URL of the pokemon infos.
    :return: All the abilities of the pokemons.
    Exemple: get_abilities_from_api('https://pokeapi.co/api/v2/abilities/1')
    """
    try:

        pokemon_id = int(endpoint_pok.split('/')[-2])
        data = connect_api(endpoint_pok)
        data_abilities = data['abilities']

        results = []
        for ab in data_abilities:
            abilitie_name = ab['ability']['name']
            abilitie_url = ab['ability']['url']
            abilitie_id_url = get_id_from_url(abilitie_url)

            if isinstance(abilitie_url, str):
                abilitie_urls = [abilitie_url]

            for url in abilitie_urls:
                get_effect = connect_api(url)
                data_effect = get_effect['effect_entries'][0]['effect']

                json_data = {
                    'abilitie_id': abilitie_id_url,
                    'name': abilitie_name,
                    'effect': data_effect
                }

                pokemon_abilities_json_data = {
                    'pokemon_id': pokemon_id,
                    'ability_id': abilitie_id_url,
                }
                query_pokemon_abilities = QUERY_INSERT['pokemon_abilities']
                store_aux_tables(pokemon_abilities_json_data, query_pokemon_abilities)

                results.append(json_data)
        logger_app_functions.info(
            f'[get_abilities_from_api] Create a JSON with the information about the Pokemons abilities: {results}')

        return results
    except Exception as e:
        logger_app_functions.error(f'[get_abilities_from_api] An error has occurred: {e} ')
        alerta(e)


def get_moves_from_api(endpoint_pok):
    """
    Get moves of the pokemons.
    :param endpoint_pok: (str) URL of the pokemon infos.
    :return: Get the information of the pokemons moves.
    Exemple: get_moves_from_api('https://pokeapi.co/api/v2/moves/1')
    """
    try:

        pokemon_id = int(endpoint_pok.split('/')[-2])
        data = connect_api(endpoint_pok)
        data_moves = data.get('moves', [])

        results = []

        for mv in data_moves:
            move_name = mv['move']['name']
            move_url = mv['move']['url']
            move_id_url = get_id_from_url(move_url)

            try:
                get_effect = connect_api(move_url)

                # Verifique se há 'effect_entries' e se a lista não está vazia
                if 'effect_entries' in get_effect and get_effect['effect_entries']:
                    effect_entry = get_effect['effect_entries'][0]
                    data_effect = effect_entry.get('effect', 'Null')
                else:
                    data_effect = 'Null'

                json_data = {
                    'move_id': move_id_url,
                    'name': move_name,
                    'effect': data_effect
                }

                pokemon_moves_json_data = {
                    'pokemon_id': pokemon_id,
                    'move_id': move_id_url,
                }
                query_pokemon_moves = QUERY_INSERT['pokemon_moves']
                store_aux_tables(pokemon_moves_json_data, query_pokemon_moves)

                results.append(json_data)

            except Exception as e:
                print(f"Erro ao conectar-se à API: {e}")
                logger_app_functions.error(f'[get_moves_from_api] An error has occurred: {e} ')

        logger_app_functions.info(
            f'[get_moves_from_api] Create a JSON with the information about the Pokemons: {results}')

        return results
    except Exception as e:
        logger_app_functions.error(f'[get_moves_from_api] An error has occurred: {e} ')
        alerta(e)


def store_pokemon_data(data, database_client, query_insert):
    """
    Stores Pokemon data in a database.

    :param data: (str) Pokemon data.
    :param database_client: (str) Database client connection
    :return: A message that the data was stored or not.

    Exemple: stored_data = store_pokemon_data(data, database_client)
    """
    try:
        # Preparando o cursor
        cursor = database_client.cursor()

        # Consulta SQL para inserir os dados na tabela pro_players
        insert_query = query_insert

        # Inserindo os dados
        for pok in data:
            cursor.execute(insert_query, pok)

        # Commit das alterações
        database_client.commit()

        # Fechando o cursor e a conexão
        cursor.close()

        logger_app_functions.info(
            f'[store_pokemon_data] Successfully stored {len(data)} Pokemon in database.')
        return f'Successfully stored {len(data)} Pokemon in database'

    except Exception as e:
        logger_app_functions.error(f'[store_pokemon_data] Failed to store {len(data)} Pokemon in database: {e}')
        return f'[store_pokemon_data] Failed to store {len(data)} Pokemon in database: {e}'


def store_aux_tables(data, query):
    """
    Stores all the data from the Pokemon aux tables.
    :param data:  (str) Pokemon data.
    :param query: (str) The query to execute.
    :return: A message that the data was stored or not.

    Exemple: stored_data = store_aux_tables(data, query)
    """
    try:
        in_client_db = connect_to_mysql()
        store_pokemon_data(data, in_client_db, query)
        disconnect_to_mysql(in_client_db)

        logger_app_functions.info(
            f'[store_aux_tables] Successfully stored {len(data)} Pokemon in aux database.')
        return f'[store_aux_tables] Successfully stored {len(data)} Pokemon in aux database.'
    except Exception as e:
        logger_app_functions.error(f'[store_aux_tables] Failed to store {len(data)} Pokemon in aux database: {e}')
        return f'[store_aux_tables] Failed to store {len(data)} Pokemon in aux database: {e}'
