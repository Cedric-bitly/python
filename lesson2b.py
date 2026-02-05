# Tuple
# A tuple is an immutable type of a list (It cannot change)
# To introduce a tuple, we use the paranthesis ()

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")
print(counties)
print(type(counties))

# Slicing of tuples
print(counties[3:])

# Accessing items of a tuple by use of the indexes
print(counties[5])
print(counties[9])

# Note below wil generate an error
# Attribute error
counties.append("Machakos")
print(counties)