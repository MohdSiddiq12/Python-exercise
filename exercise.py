# Simple function definition
def greet(name):
    return f"Hello, {name}!"

# Function call
result = greet("Alice")
print(result)


# Function with default parameter
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Function call without specifying greeting
result = greet("Bob")
print(result)

# Function call with a custom greeting
result_custom = greet("Charlie", "Hi")
print(result_custom)


# Function returning multiple values
def get_circle_info(radius):
    circumference = 2 * 3.14 * radius
    area = 3.14 * radius ** 2
    return circumference, area

# Function call and unpacking results
circumference, area = get_circle_info(5)
print(f"Circumference: {circumference}, Area: {area}")

# Recursive function for factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Function call
result_factorial = factorial(5)
print(f"Factorial of 5 is {result_factorial}")

# Higher-order function that takes a function as an argument
def apply_operation(x, y, operation):
    return operation(x, y)

# Functions to pass as arguments
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Function calls
result_add = apply_operation(3, 4, add)
result_multiply = apply_operation(3, 4, multiply)

print(f"Addition result: {result_add}")
print(f"Multiplication result: {result_multiply}")
