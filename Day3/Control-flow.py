# Topics to Cover
# Conditional Statements
# Loops
# Learning Objectives
# Understand how to use if, elif, and else statements.
# Learn how to use for and while loops to iterate over sequences and execute code repeatedly.
# Practice using break and continue statements to control loop execution

# Simple if Statement:
# Write a Python program that checks if a number is positive, negative, or zero and prints an appropriate message.

# number = int(input("enter a number"))
# if number >= 1:
#     print('number is positive')
# elif number <= -1:
#     print("number is negative")
# else:
#     print("number is zero")

# if-elif-else Statement:
# Write a Python program that asks the user for their age and prints whether they are a child, teenager, adult, or senior.

# age = int(input("enter your age: "))
# if age <= 5:
#     print("You are child")
# elif age <= 18:
#     print("you are teenager")
# elif age <= 40:
#     print("you are an adult")
# else:
#     print("you are senior")

# Nested if Statements:
# Write a Python program that checks if a number is even or odd and if it is divisible by 3.

# number = int(input("enter a number: "))
# if number%2 == 0:
#     print("number is even")
#     if number %3 == 0:
#         print("number is even and is divisible by 3")
#     else:
#         print("number is even and not divisible by 3")
# else:
#     print("number is odd")
#     if number%3 == 0:
#         print("number is odd and is divisible by 3")
#     else:
#         print("number is odd and is not divisible by 3")


# for Loop:
# Write a Python program to print the first 10 natural numbers using a for loop.

for i in range(1,11):
    print(i)