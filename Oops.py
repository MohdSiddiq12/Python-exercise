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