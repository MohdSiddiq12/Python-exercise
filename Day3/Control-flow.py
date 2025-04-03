# Topics to Cover
# Conditional Statements
# Loops
# Learning Objectives
# Understand how to use if, elif, and else statements.
# Learn how to use for and while loops to iterate over sequences and execute code repeatedly.
# Practice using break and continue statements to control loop execution

# Simple if Statement:
# Write a Python program that checks if a number is positive, negative, or zero and prints an appropriate message.
number = int(input("enter a number"))
if number >= 1:
    print('number is positive')
elif number <= -1:
    print("number is negative")
else:
    print("number is zero")
number = int(input("enter a number"))
if number >= 1:
    print('number is positive')
elif number <= -1:
    print("number is negative")
else:
    print("number is zero")

# if-elif-else Statement:
# Write a Python program that asks the user for their age and prints whether they are a child, teenager, adult, or senior.

age = int(input("enter your age: "))
if age <= 5:
    print("You are child")
elif age <= 18:
    print("you are teenager")
elif age <= 40:
    print("you are an adult")
else:
    print("you are senior")

# Nested if Statements:
# Write a Python program that checks if a number is even or odd and if it is divisible by 3.

number = int(input("enter a number: "))
if number % 2 == 0:
    print("number is even")
    if number % 3 == 0:
        print("number is even and is divisible by 3")
    else:
        print("number is even and not divisible by 3")
else:
    print("number is odd")
    if number % 3 == 0:
        print("number is odd and is divisible by 3")
    else:
        print("number is odd and is not divisible by 3")


# for Loop:
# Write a Python program to print the first 10 natural numbers using a for loop.

for i in range(1, 11):
    print(i)

# while Loop:
# Write a Python program to print the numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i)
    i += 1


# Break Statement:
# Write a Python program that iterates through numbers from 1 to 10 and stops the loop if the number is 5.

for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Continue Statement:
# Write a Python program that iterates through numbers from 1 to 10 and skips printing the number 5.

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Nested Loops:
# Write a Python program to print a multiplication table for numbers from 1 to 5 using nested loops.

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} * {j} == {i * j}")