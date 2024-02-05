# Class and Object
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name},says woof!")
# Creating an object
my_dog = Dog("Buddy", 3)
print(my_dog.name)
my_dog.bark()

#explanation 
#Dog is the name of the class.
#__init__ is a special method (constructor) that gets called when an object is created. It initializes the attributes of the object.
#self is a reference to the instance of the class (the object itself).
#name and age are attributes of the class.

#Objects:
#An object is an instance of a class. It is a concrete entity created from the class blueprint. 
#Objects have attributes (characteristics) and methods (functions) associated with them.
class method:
    def __init__(self):
        print("hello from method")
    
x = method()
print(x)

#Class Variables vs. Instance Variables:
#Class Variables: Shared by all instances of a class. Defined outside any method.

class Dog:
    legs = 4  # Class variable

# Accessing class variable
print(Dog.legs)  # Output: 4

#Instance Variables: Belong to a specific instance of the class. Defined inside the __init__ method.


class Dog:
    def __init__(self, name):
        self.name = name  # Instance variable

# Creating an object
my_dog = Dog("Buddy")

# Accessing instance variable
print(my_dog.name)  # Output: Buddy


#What is a Constructor?
#A constructor is a method that is automatically called when an object is instantiated from a class. 
# It is named __init__ and is used to initialize the attributes of the object.
#  The self parameter refers to the instance of the class, 
# and it allows you to access the object's attributes and methods within the class.

#How to Define a Constructor:

class MyClass:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
#The __init__ method is defined with the self parameter and additional parameters (parameter1, parameter2 etc).
#Inside the constructor, attributes of the object are initialized using self.attribute = parameter.
#Example:

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes initialized in the constructor
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3

#In this example, the __init__ method is used to initialize the name,
#and age attributes of the Dog class when an object is created.

#Default Values in Constructors:
#You can provide default values for parameters in the constructor, making them optional during object creation.


class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

# Creating objects with and without specifying parameters
person1 = Person()
person2 = Person("Alice", 25)

print(person1.name, person1.age)  # Output: Unknown 0
print(person2.name, person2.age)  # Output: Alice 25
#In this example, if no values are provided during object creation, the default values will be used.

#Multiple Constructors (Overloading in Python):
#While Python does not support method overloading in the traditional sense,
#you can achieve a similar effect by providing default values for some parameters.


class Example:
    def __init__(self, parameter1, parameter2=None):
        if parameter2 is None:
            # This block gets executed if parameter2 is not provided
            self.attribute1 = parameter1
            self.attribute2 = "Default"
        else:
            # This block gets executed if parameter2 is provided
            self.attribute1 = parameter1
            self.attribute2 = parameter2
#In this example, you can create an object with either one or two parameters.

#Constructors are essential in object-oriented programming as they allow you to set up 
#the initial state of an object. They provide a way to initialize attributes and ensure that
#objects are in a valid state when created. 



In object-oriented programming (OOP), nested classes refer to the concept of defining one class inside another class. The class that contains another class is called the outer class, and the class inside it is referred to as the inner class or nested class. This concept allows you to organize and encapsulate related functionality within a class hierarchy.

Let's go through an example to illustrate nested classes in Python:

python
Copy code
class OuterClass:
    def __init__(self, outer_attribute):
        self.outer_attribute = outer_attribute

    def outer_method(self):
        print("This is the outer method.")

    class InnerClass:
        def __init__(self, inner_attribute):
            self.inner_attribute = inner_attribute

        def inner_method(self):
            print("This is the inner method.")

# Creating an object of the outer class
outer_obj = OuterClass("Outer Attribute")

# Accessing outer class attributes and methods
print(outer_obj.outer_attribute)  # Output: Outer Attribute
outer_obj.outer_method()            # Output: This is the outer method.

# Creating an object of the inner class using the outer class
inner_obj = outer_obj.InnerClass("Inner Attribute")

# Accessing inner class attributes and methods
print(inner_obj.inner_attribute)  # Output: Inner Attribute
inner_obj.inner_method()          # Output: This is the inner method

