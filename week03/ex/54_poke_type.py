import requests


def poke_type(type_list):
	''' Searching for the match pokemon type in json
		Arg: List of string type of pokemon
		Return: List of tuple contain pokemon in the mention type with ID and NAME
	'''
	endpoint_url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
	try:
		pokemon_req = requests.get(endpoint_url)
	except requests.exceptions.ConnectionError as e:
		print("Please connection to the internet!")
		return res_list
		exit()
	else:
		pokemon_dict = pokemon_req.json()['pokemon']
		res_list = list()
		given_type = list()
		for each_type in type_list:
			given_type.append(each_type.capitalize())
		for each_pokemon in pokemon_dict:
			if given_type == each_pokemon['type']:
				res_tuple = (each_pokemon['id'], each_pokemon['name'])
				res_list.append(res_tuple)
		return res_list
	

# print(poke_type(['grAss','fIrE']))
# print(poke_type(['PsyChic']))
# print(poke_type(['waTer', 'PsyChic']))
# print(poke_type(['waTer', 'FiRe']))
# print(poke_type("sd"))

