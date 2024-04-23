import os
import logging
from plyer import notification


def configurar_logger(nome_logger, nome_arquivo):
    """
        Configures a logger to record messages in a log file.

        Parameters:
        - logger_name (str): The name of the logger to be configured.
        - file_name (str): The name of the log file to be created and used for logging messages.

        Returns:
        - logging.Logger: A configured logger object to record messages in a file.

        Example:
            logger = configure_logger('my_logger', 'my_file.log')
            logger.info("This is an example of a log message.")
    """
    # Caminho absoluto para a pasta 'logs' na raiz do projeto
    caminho_logs = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))

    # Criar a pasta 'logs' se ela não existir
    if not os.path.exists(caminho_logs):
        os.makedirs(caminho_logs)

    # Caminho absoluto para o arquivo de log
    caminho_arquivo = os.path.join(caminho_logs, nome_arquivo)

    logger = logging.getLogger(nome_logger)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(caminho_arquivo)
    file_handler.setLevel(logging.INFO)

    # Definir o formato de log para incluir data e hora
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


def alerta(erro):
    """
    Alert error on the screen.
    :param erro: (str) Error message.
    :return: Error message.
    Exemple: alerta('Error for connect to the API')
    """
    return notification.notify(
        title='Pokemon API',
        message=f'An error occurred while connecting to the Pokemon API: {erro}',
        app_name='Pokeapi',
        timeout=10
    )
