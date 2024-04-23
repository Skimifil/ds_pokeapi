from src.logger import *
from src.connect_api import connect_api
from src.connect_database import *


def get_id_from_url(url):
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

        return results
    except Exception as e:
        alerta(e)


def get_abilities_from_api(endpoint_pok):
    """
    Get abilities of the pokemons.
    :param endpoint_pok: (str) URL of the pokemon infos.
    :return: All the abilities of the pokemons.
    Exemple: get_abilities_from_api('https://pokeapi.co/api/v2/abilities/1')
    """
    try:

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

                results.append(json_data)

        return results
    except Exception as e:
        alerta(e)


def get_moves_from_api(endpoint_pok):
    """
    Get moves of the pokemons.
    :param endpoint_pok: (str) URL of the pokemon infos.
    :return: Get the information of the pokemons moves.
    Exemple: get_moves_from_api('https://pokeapi.co/api/v2/moves/1')
    """
    try:

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

                results.append(json_data)

            except Exception as e:
                print(f"Erro ao conectar-se à API: {e}")

        return results
    except Exception as e:
        alerta(e)
