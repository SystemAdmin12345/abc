import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power,
    '%': modulo
}

def evaluate(expression):
    stack = []
    for token in expression:
        if token in operations:
            b = stack.pop()
            a = stack.pop()
            stack.append(operations[token](a, b))
        else:
            stack.append(token)
    return stack.pop()

def main():
    expression = input('Enter an expression: ')
    result = evaluate(expression)
    print(result)