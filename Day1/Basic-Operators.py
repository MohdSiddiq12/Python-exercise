#Variable and Data Types:
#Write a Python program that takes the user's name as input and greets them with "Hello, [name]!"

name = input("enter your name: ")
print("hello " + name, "Good Morning")

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

#Input/Output:
#Write a Python program that asks the user for their age and then prints out the age.

age = int(input("enter your age: "))
print("Your age is ", age)

#Conditional Statements:
# Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

number = int(input("enter any number: "))
if number >= 1:
    print("number is positive")
elif number <= -1:
    print("number is negative")
else:
    print("number is zero")

# Loops:
# Write a Python program to print all the even numbers from 1 to 20.

n = 20
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

#Lists:
# Write a Python program to create a list of 5 colors and then print each color on a new line.

colors = ['red', 'green', 'blue', 'yellow', 'black']
for i in colors:
    print(i)

#Tuples:
# Write a Python program that creates a tuple of your favorite fruits and then prints them.

myfruits = ("grapes", "apple", "mango", "pineapple", "guava")
for i in myfruits:
    print(i)

# Dictionaries:
# Write a Python program that creates a dictionary with students' names as keys and their ages as values. Then print out each student's name and age.

# dictionary syntax dict_var = {key1 : value1, key2 : value2, …..}
dict = {"John": 21, "abraham": 23, "joshua": 22}
for name, age in dict.items():
    print(name + ":", age)

#Sets:
# Write a Python program that takes two sets as input and prints the intersection, union, and difference of the sets.

# Taking input for the first set
set1_input = input("Enter elements of the first set separated by commas: ")
set1 = set(item.strip() for item in set1_input.split(','))

# Taking input for the second set
set2_input = input("Enter elements of the second set separated by commas: ")
set2 = set(item.strip() for item in set2_input.split(','))

# Printing the intersection, union, and difference of the sets
print("Intersection:", set1.intersection(set2))
print("Union:", set1.union(set2))
print("Difference (Set1 - Set2):", set1.difference(set2))
print("Difference (Set2 - Set1):", set2.difference(set1))

#Functions
# Write a Python program that defines a function to calculate 
# the area of a rectangle given its length and width.
#  Prompt the user for the length and width and then print the area

def area_of_rectangle(length, width):
    rectangle = length * width
    return rectangle

length = float(input("enter the length"))
width = float(input("enter the width"))

area = area_of_rectangle(length, width)

print(area)
