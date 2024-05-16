#Variable and Data Types:
#Write a Python program that takes the user's name as input and greets them with "Hello, [name]!"

# 

#Basic Operators:
#Write a Python program that prompts the user to enter two numbers and then performs addition, subtraction,
# multiplication, and division on those numbers, printing the results.

x = float(input("enter x "))
y = float(input("enter y "))

addition = x + y
subtraction = x - y
multiplication = x * y
if y != 0:
    division = x / y
else:
    print("cannot divide by zero")


print("addition", x, "+",  y, "=", addition)
print("subtraction", x, "-", y, "=", subtraction)
print("multiplication",  x, "*",  y, "=", multiplication)
print("division",  x, "/",  y, "=", division)