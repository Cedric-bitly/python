# Loops -> sometime we may need to do a piece of work a number of repeated times in such cases we may use loop
# A loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met.
# There are two types of loops in python i.e; The for loop and the while loop

# Below is the syntax of a loop in python
"""
for variable in range(n):
     # block of code to be executed
"""

# print("Hello, Moses")
# print("Hello, Moses")
# print("Hello, Moses")
# print("Hello, Moses")
# print("Hello, Moses")

for greeting in range(5):
    print("Hello Moses")
    

print('----------------------')

for number in range(11,21):
    print(number)

print('----------------------')
# Find the even numbers in the rango of 50 to 71
for number in range(50, 71 ,2):
    print(number)


print('----------------------')
# Create a python program that prints the odd number from 100 to 150
for num in range(101, 150, 2):
    print(num)

print('----------------------')    
 # create a program that prints the multiples of 3 starting from 201 to 150   
for num in range(201, 149, -3):
    print(num)

print('----------------------')
# Create a python program that prints the leap in between 2000 and 2024
# Method 1: Using leap year logic
for year in range(2000, 2025):
    if  (year % 4 == 0 and year % 100 != 0):
        print(year)