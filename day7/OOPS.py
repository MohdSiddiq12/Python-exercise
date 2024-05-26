# For Day 7, let's focus on mastering object-oriented programming (OOP) in Python.
# OOP is a programming paradigm based on the concept of "objects,"
#  which can contain data and code that manipulates that data. Understanding OOP principles is essential for 
# designing and implementing complex systems in a structured and reusable way.

# Topics to Cover
# Classes and Objects
# Attributes and Methods
# Inheritance
# Polymorphism
# Encapsulation
## Learning Objectives
# Understand how to define and create classes and objects.
# Learn how to define and use attributes and methods.
# Understand inheritance and how to create subclasses.
# Learn about polymorphism and how to implement it.
# Understand encapsulation and how to manage access to an object's attributes and methods.
# Exercises
# Classes and Objects
# Define a Class:
# Write a Python class called Dog that has attributes for name, age, and breed. Create an object 
#of this class and print its attributes.

# class dog():
# #     def __init__(self,name,age,breed):
# #         self.name = name
# #         self.age = age
# #         self.breed = breed
# # my_dog = dog('husky',2,'asian')
# print(f"{my_dog.name},{my_dog.age},{my_dog.breed}")

# Methods:
# Add a method called bark to the Dog class that prints a barking sound. Call this method from an object of the class.

# class dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print("dog says woof!!")
# my_dog = dog('husky',3)
# print(f"{my_dog.name},{my_dog.age}")
# my_dog.bark()


# Inheritance
# Inheritance:
# Write a Python class called Animal with attributes for species and age. 
# Create a subclass called Cat that inherits from Animal and adds an attribute for breed. 
# Create an object of the Cat class and print its attributes.

# class Animal():
#     def __init__(self,species,age):
#         self.species = species
#         self.age = age

# class Cat(Animal):
#     def __init__(self,species,age,breed):
#         super().__init__(species,age)
#         self.breed = breed
        

# cat = Cat("burglar",4,"persian")
# print(f"{cat.species},{cat.age},{cat.breed}")
# Polymorphism
# Polymorphism:
# Write two classes, Rectangle and Circle, each with a method called area that calculates and returns the area of the shape. 
# Write a function that takes an object of either class and prints the area.
# class Rectangle():
#     def __init__(self,l,w):
#         self.l = l
#         self.w = w 
#     def area(self):
#         return self.l * self.w

# class Circle():
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         return 3.14 * self.r * self.r


# def print_area(shape):
#     print(f"The area is: {shape.area()}")

# rectangle = Rectangle(1,2)
# circle = Circle(2)

# print_area(rectangle)
# print_area(circle)
# Encapsulation
# Encapsulation:
# Write a Python class called BankAccount with private attributes for account number and balance.
# Add methods to deposit and withdraw money, and to get the current balance. Use getters and setters to access 
# and modify the private attributes.