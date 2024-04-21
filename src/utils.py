from src.logger import configurar_logger
from src.connect_api import connect_api
from src.connect_database import *


def get_data_from_api(url):
    name_of_pokemons = connect_api(url)

