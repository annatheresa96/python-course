my_stats = {
    "name" : "Anna",
    "age" : "25",
    "occupation" : "Tester",
}
print(my_stats)
my_stats["location"] = "Berkshire"
print(my_stats)
del my_stats["location"]
print(my_stats)
my_stats["occupation"] = "Support"
print(my_stats)
print(my_stats["name"])

my_pokemon = {
    "pokemon" : "Rapidash",
    "type" : "Fire",
    "level" : "30",
}
my_pokemon["move"] = "Flame Wheel"
print(my_pokemon)
for value in my_pokemon.values():
    print (value)
for key in my_pokemon.keys():
    print(key)
my_pokemon["move"] = "Flame Wheel", "Agility"
print(my_pokemon)
print(my_pokemon["move"][0])
print(my_pokemon["move"][1])