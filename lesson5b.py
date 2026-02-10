# Functions with Parameters.
# They are values that get passed as arguement given to a function inside of the paranthesis.


def greeting(name):
    print(f"{name} How are you? Hope everything is fine?")

greeting("Cedric")
greeting("Sandra")

print("====================")
def message(names):
    print(f"Hello {names}. We shall be having a General Annual Meeting")

message("Joy")
message("Harriet")


print("====================")
# Create a function that accepts parameters to add two numbers
def add_numbers(num1, num2):
    sum = num1 + num2
    print(f"The sum is: {sum}")

add_numbers(10, 20 ) 

print("====================")
