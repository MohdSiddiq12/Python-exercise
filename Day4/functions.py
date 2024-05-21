# Topics to Cover
# Functions
# Function Parameters
# Return Statement
# Modules
# Importing Modules
# Learning Objectives
# Understand how to define and call functions.
# Learn about function parameters and their types (positional, keyword, default, variable-length).
# Understand the purpose and usage of the return statement.
# Learn how to create and use modules to organize code.
# Exercises
# Functions
# Simple Function:
# Write a Python function that takes two numbers as input and returns their sum.
# def add(x,y):
#     return x + y
# num = add(1,2)
# print(num)

# Function with Parameters:
# Write a Python function that takes a list of numbers as input and returns the maximum value from the list.
# def maximum(*args):
#     return max(*args)
# num = maximum(1,2,3,4,5,6,11,22,33,44)
# print(num)

# Return Statement
# Function with Return Statement:
# Write a Python function that checks if a number is prime and returns True if it is, False otherwise.

# def is_prime(num):
#     if num <= 1:
#         return False
#     elif num == 2:
#         return True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False

#     return True
# number = 11
# if is_prime(number):
#     print(f"{number} is prime.")
# else:
#     print(f"{number} is not prime.")

# Import Module:
# Write a Python program that imports the calculator.py module and uses its functions to perform arithmetic operations.
import calculator

print("addition",calculator.add(1,2))
print("subtractiom",calculator.subtraction(1,2))
print("multiplication",calculator.multiplication(1,2))
print("division",calculator.division(1,2))