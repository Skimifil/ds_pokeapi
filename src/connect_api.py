import requests
from src.logger import configurar_logger

logger_api_connection = configurar_logger("api_connection",
                                          "api_connection.log")


def connect_api(url):
    """
    Connects to API and returns de data from endpoint.

    :param url: (str) url to connect.
    :return: Data from API.

    Exemple: data = connect_api('https://pokeapi.co/api/v2/pokemon/?limit=1')
    """
    try:
        logger_api_connection.info(f"[connect_api] Connected to the API.")
        response = requests.get(url)
        data = response.json()

        if 'results' in data:
            logger_api_connection.info(f"[connect_api] Data return: {data}")
            return data['results']
        else:
            logger_api_connection.info(f"[connect_api] Data return: {data}")
            return data

    except Exception as e:
        logger_api_connection.error(f"[connect_api] Error connecting to API, error: {e}.")
        return f"[connect_api] Error connecting to API, error: {e}."
