# For loop
# A for loop can also be used to iterate through a list, tuple, string or even a dictionary.
 
player  = {
    "name" : "Mbappe",
    "age" : 25,
    "teams" : ["PSG", "Monaco", "France"],
    "nationality" : "French"
}

for key in player:
    print(key)
print("=============")
for values in player:
    print(player[values])

print("=============")
for team in player["teams"]:
    print(team)