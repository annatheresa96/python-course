my_data = {
    "name":"Anna",
    "occupation":"Tester"
}
print(my_data)

my_info = dict(name = "Anna", occupation = "Tester")
print(my_info)

my_Data = {}
print(my_Data)
my_Data = dict
print(my_Data)

my_data["location"] = "Berkshire"
print(my_data)
my_data["occupation"] = "Support"

print(my_data['location'])
print(my_data.get('location'))

#my_data.clear()
#print(my_data)

#del my_data["location"]
#print(my_data)

for key in my_data:
    print("Key: " + key)

for key in my_data.keys():
    print(key)

for value in my_data.values():
    print ("Value: " + value)

for key,value in my_data.items():
    print("Key: " + key + ", value: " + value)

for key,value in my_data.items():
    print(key + " " + value)

students = {
    "Student 1": {
        "Name" : "Anna",
        "Age" : "25", 
    },
    "Student 2": {
        "Name" : "Henrietta",
        "Age" : "23",
        "Shopping" : ("apple", "pear")
    }
}
print(students["Student 1"]["Name"])
print(students["Student 2"]["Shopping"][0])

print(students[0])["Name"]