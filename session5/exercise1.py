pokemon = ["Pikachu","Squirtle","Charizard","Snorlax"]
print(pokemon)
pokemon.insert(1, "Eevee")
print(pokemon)
pokemon.remove("Eevee")
print(pokemon)
print(pokemon[2])
my_team = ["Landorus", "Weedle", "Spearow", "Pidgey", "Gardevoir"]
pokedex = [pokemon + my_team]
print(pokedex)
pokedex.insert(2, "Rattata")
print(pokedex)
pokedex_length = len(pokedex)
print(pokedex_length)
for item in pokedex:
    print(item)
if "Charizard" in pokedex:
    print("Charizard is in the pokedex")

