# A dictionary is a data type that stores data in terms of key - value pair.
# It is introduced by the use of curly braces {}
# The values stored inside of a dictionary can be of any data type
# To acces the values in a dictionary we use the keys


phonebook = {
    "Benson" : "+25470000",
    "Judy" : "+25470000",
   "Benson" : "+245700000"
}
print(phonebook)
print(type(phonebook))

# print out Benson's number
print(phonebook["Benson"])


player = {
    "name" : "Messi",
    "age" : 40,
    "team" : ["Barcelona", "PSG", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : (784778566, 76767667, 989283446)
    }
    }
print(player["team"][0])
print(player["more"]["phone"][1])
