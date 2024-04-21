from src.logger import configurar_logger
from src.connect_api import connect_api
from src.connect_database import *


def get_pokemon_from_api():
    data = connect_api(f'https://pokeapi.co/api/v2/pokemon/?limit=1')
    return data[0]['url']


def get_abilities_from_api(endpoint_pok):
    data = connect_api(endpoint_pok)
    data_abilities = data['abilities']

    results = []
    for ab in data_abilities:
        abilitie_name = ab['ability']['name']
        abilitie_url = ab['ability']['url']

        if isinstance(abilitie_url, str):
            abilitie_urls = [abilitie_url]

        for url in abilitie_urls:
            get_effect = connect_api(url)
            data_effect = get_effect['effect_entries'][0]['effect']

            json_data = {
                'name': abilitie_name,
                'url': abilitie_url,
                'effect_description': data_effect
            }

            results.append(json_data)

    return results
