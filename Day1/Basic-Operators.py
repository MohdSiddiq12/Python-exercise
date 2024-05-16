#Variable and Data Types:
#Write a Python program that takes the user's name as input and greets them with "Hello, [name]!"

# 

#Basic Operators:
#Write a Python program that prompts the user to enter two numbers and then performs addition, subtraction,
# multiplication, and division on those numbers, printing the results.

# x = float(input("enter x "))
# y = float(input("enter y "))

# addition = x + y
# subtraction = x - y
# multiplication = x * y
# if y != 0:
#     division = x / y
# else:
#     print("cannot divide by zero")


# print("addition", x, "+",  y, "=", addition)
# print("subtraction", x, "-", y, "=", subtraction)
# print("multiplication",  x, "*",  y, "=", multiplication)
# print("division",  x, "/",  y, "=", division)

#Input/Output:
#Write a Python program that asks the user for their age and then prints out the age.

# age = int(input("enter your age: "))
# print("Your age is ",age)

#Conditional Statements:
# Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

# number = int(input("enter any number: "))
# if number >= 1:
#     print("number is positive")
# elif number <= -1:
#     print("number is negative")
# else:
#     print("number is zero")

# Loops:
# Write a Python program to print all the even numbers from 1 to 20.

# n = 20
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i)
    

#Lists:
# Write a Python program to create a list of 5 colors and then print each color on a new line.

# colors = ['red','green','blue','yellow','black']
# for i in colors:
#     print(i)

#Tuples:
# Write a Python program that creates a tuple of your favorite fruits and then prints them.

# myfruits = ("grapes","apple","mango","pineapple","guava")
# for i in(myfruits):
#     print(i)

# Dictionaries:
# Write a Python program that creates a dictionary with students' names as keys and their ages as values. Then print out each student's name and age.

# dictionary syntax dict_var = {key1 : value1, key2 : value2, …..}
dict = {"John": 21, "abraham": 23, "joshua": 22}
for name,age in dict.items():
    print(name + ":", age)