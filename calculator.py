'''
Create a menu-driven calculator that lets the user choose an operation (add, subtract, multiply, divide), enter two numbers, and get the result.
'''

operators = ["add", "subtract", "multiply", "divide"]

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def user_input():
    operation = input("Choose operation: ")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return operation, x, y

def calculate():
    operation, x, y = user_input()
    if operation not in operators:
        print(f"{operation} is not a valid operator. Try again")
        calculate()
    elif operation == "add":
        return add(x, y)
    elif operation == "subtract":
        return subtract(x, y)
    elif operation == "multiply":
        return multiply(x, y)
    elif operation == "divide":
        if y == 0:
            print("You can't divide by 0")
        return divide(x, y)

print(calculate())
# print(subtract(8,3))