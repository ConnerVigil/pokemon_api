import requests

print("----------Welcome to the Pokemon API----------")
print()

pokemonType = input("Please input the pokemon type you would like to query: ")

url = "https://pokeapi.co/api/v2/pokemon/" + pokemonType + "/"
print(url)

response = requests.get(url)

print(response.json())
