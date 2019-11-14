import requests, os

def poke_gallery():
	''' Create a gallery of pokemon character
		Arg:
		Return:
	'''

	endpoint_url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
	html_file = "pokemon.html"
	pokemon_req = requests.get(endpoint_url)
	pokemon_dict = pokemon_req.json()['pokemon']
	with open(html_file, "w+") as file:
		# file.write("<html><body>")
		for each_pokemon in pokemon_dict:
			pokemon_img = each_pokemon['img']
			file.write(f"<img src=\"{pokemon_img}\" height=\"100px\" width=\"100px\">")
		# file.write("</body></html>")


poke_gallery()