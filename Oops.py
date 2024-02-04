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
