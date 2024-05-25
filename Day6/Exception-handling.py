# Topics to Cover
# Basics of exception handling
# Common exceptions
# try, except, else, and finally blocks
# Raising exceptions
# Custom exceptions
# Learning Objectives
# Understand how to handle exceptions using try and except.
# Learn about different types of exceptions and how to handle multiple exceptions.
# Understand the use of else and finally in exception handling.
# Learn how to raise exceptions manually.
# Understand how to define and use custom exceptions.
# Exercises
# Basics of Exception Handling
# Basic Try/Except:
# Write a Python program that takes two numbers as input from the user and performs division. Use a try/except block to handle any potential division by zero errors.
# try:
#     x = int(input("enter a number"))
#     y = int(input("enter a number"))
#     result = x / y
#     print(result)
# except ZeroDivisionError:
#     print("cannot divide by zero ")


# Handling Multiple Exceptions:
# Write a Python program that takes a list of numbers as input from the user. Use a try/except block to handle both ValueError and TypeError exceptions.

# try:
#     numbers = input("enter numbers seperated by spaces").split()
#     numbers = [int(num) for num in numbers]
#     total = sum(numbers)
#     print("sum",total)
# except ValueError:
#     print('value error')
# except TypeError:
#     print("type error")
# Else and Finally
# Try/Except/Else:
# Write a Python program that reads a file. Use a try/except block to handle any potential FileNotFoundError.
# If no exception occurs, print "File read successfully." Use the else block for this message.

try:
    with open('Day5\destination.txt','r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('file not found')
else:
    print("file read successfully")
# Try/Except/Finally:


# Write a Python program that opens a file and writes some data to it. Use a try/except block to handle any potential I/O errors. Ensure that the file is always closed after the operation using the finally block.

# Raising Exceptions
# Raise Exception:
# Write a Python function that takes a number as input and raises a ValueError if the number is negative.
# Custom Exceptions
# Custom Exception:
# Define a custom exception called NegativeNumberError. Write a Python function that takes a number as input and raises this custom exception if the number is negative.