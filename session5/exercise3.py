my_dict = dict()
my_dict = {
    "pokemon" : "Bulbasaur",
    "type" : "Grass",
    "level" : "5",
}
print(my_dict)
my_dict["moves"] = "Vine whip" , "Razor leaf" , "Growl" , "Cut"
print(my_dict)
my_dict["level"] = "10"
print(my_dict)
moves = ["Vine whip" , "Razor leaf" , "Growl" , "Cut"]
if "Cut" in moves:
    print("Cut move exists")