from src.connect_api import connect_api

if __name__ == '__main__':
    teste = connect_api('https://pokeapi.co/api/v2/pokemon/?limit=1')
    print(teste)
