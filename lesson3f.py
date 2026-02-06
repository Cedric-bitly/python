# Create a pyhton program that is able to  determine whether a number entered is an odd number or even number

#number = int(input("Enter a number: "))

#if number % 2 == 0:
    #print("The number is EVEN")
#else:
    #print("The number is ODD")

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person. If the weight is greayer thab 50kgs and age is above 18 else not possible

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

if age >= 18 and weight >= 50:
    print("You are fit to donate blood.")
else:
    print("You are not fit to donate blood.")