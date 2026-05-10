# Beginning of my journey


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None
    return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

op = input("Enter operation (+, -, *, /): ")
if op in operations:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = operations[op](num1, num2)
    print(f"Result: {result}")
else:
    print("Invalid operation")