# Task 1
#for year in range(2000, 2025):
    #print(year)
#print("====================")
#year = 2000
#while year <= 2024:
   # print(year)
   # year += 1

#print("====================")
# Task 2
#colors = ["Blue", "Green", "Red", "Pink", "Black"]
#for color in colors:
    #print(color)

#print("====================")
# Task 3
#count = 20
#while count >= 1:
    #print(count)
   # count -= 1

#print("====================")


print("====================")

# Python Day 5

# Question 1(Function without Parameters)
def area():
    l = 17
    w = 13
    A = l * w
    print(f"The area of the rectangle is: {A}")

area()

print("====================")

# Question 2(Function With Parameters)
def calculate(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    division = num1 / num2
    return sum, difference, product, division

# Call the function
sum, diff, prod, div = calculate(437, 303)

print(f"The sum of the two numbers is: {sum}")
print(f"The difference of the two numbers is: {diff}")
print(f"The product of the two numbers is: {prod}")
print(f"The division of the two numbers is: {div}")

print("====================")

# Question3(Control Statement (if...elif...else))
def check_number():
    num = int(input("Enter a number: "))
    
    if num > 0:
        print(f"{num} is a positive number")
    elif num < 0:
        print(f"{num} is a negative number")
    else:
        print(f"{num} is zero")

check_number()

print("====================")

# Question4(Loop with Arithmetic)
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"The sum of numbers from 1 to {n} is: {total}")

sum_of_numbers(20)

print("====================")

# Question5()
def calculate_squares():
    n = int(input("Enter a number: "))
    
    i = 1
    while i <= n:
        square = i * i
        print(f"The square of {i} is: {square}")
        i += 1

calculate_squares()