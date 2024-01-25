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
