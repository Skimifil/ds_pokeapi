import mysql.connector
from src.config import MYSQL_CONFIG
from src.logger import configurar_logger
from src.utils import alerta


logger_db_connect = configurar_logger("connection_db_mysql", "connection_db_mysql.log")


def connect_to_mysql():
    """
    Connects to the MySQL database.

    :return: Connection object.
    Exemple: conexao = connect_to_mysql()
    """
    try:

        logger_db_connect.info(f"[connect_to_mysql] Connecting to MySQL database...")
        usuario = MYSQL_CONFIG['MYSQLUSER']
        senha = MYSQL_CONFIG['MYSQLPASSWORD']
        host = MYSQL_CONFIG['MYSQLSERVER']
        banco = MYSQL_CONFIG['MYSQLDB']
        # Connect to MySQL
        conn = mysql.connector.connect(
            host=host,
            port=3306,
            user=usuario,
            password=senha,
            database=banco
        )

        print(f"[connect_to_mysql] Connection success to MySQL!")
        logger_db_connect.info(f"[connect_to_mysql] Connection success to MySQL!")
        return conn

    except mysql.connector.Error as e:
        logger_db_connect.error(f"[connect_to_mysql] Error on connection to MySQL: {e}")
        alerta(f"[connect_to_mysql] Error on connection to MySQL: {e}")
        print(f"[connect_to_mysql] Error on connection to MySQL: {e}")


def disconnect_to_mysql(conn):
    """
    Disconnects from the MySQL database.

    :param conn: (str) Connection object.
    :return: None

    :Exemple: disconnect = disconnect_to_mysql(conn)
    """
    if conn:
        conn.close()

        logger_db_connect.info(f"[disconnect_to_mysql] Client disconnected!")
        print(f'[disconnect_to_mysql] Client disconnected!')
    else:
        logger_db_connect.error(f"[disconnect_to_mysql] Client error. Error: {conn}")
        return f'Client error. Error: {conn}'
