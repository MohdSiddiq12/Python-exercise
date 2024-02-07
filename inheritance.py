#basic inheritance
#inheritance is the concept of creating a new class based on an existing class.
#In this example, we have two classes: Animal and Dog.
class Animal:
    def __init__(self,species):
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("woo!!")

my_Animal = Animal("Mehd")
my_dog = Dog("khaled")

print(my_dog.species)
print(my_Animal.species)