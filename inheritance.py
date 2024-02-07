#basic inheritance
#inheritance is the concept of creating a new class based on an existing class.
#In this example, we have two classes: Animal and Dog.
class Animal:
    def __init__(self,species):
        self.species = species

    class makesound(self):
        
            print("some animal sound")

class Dog(Animal):
    def bark(self):
        print("woo!!")

my_Animal = Animal('Mehd')
my_dog = Dog('khaled')