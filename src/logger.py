import logging
import os


def configurar_logger(nome_logger, nome_arquivo):
    """
        Configura um logger para registrar mensagens em um arquivo de log.

        Parâmetros:
        - nome_logger (str): O nome do logger a ser configurado.
        - nome_arquivo (str): O nome do arquivo de log a ser criado e usado para registrar mensagens.

        Retorna:
        - logging.Logger: Um objeto de logger configurado para registrar mensagens em um arquivo.

        Exemplo:
            logger = configurar_logger('meu_logger', 'meu_arquivo.log')
            logger.info("Este é um exemplo de mensagem de log.")
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
