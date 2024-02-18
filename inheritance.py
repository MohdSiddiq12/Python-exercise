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

#multiple inheritance
#Multiple inheritance allows a class to inherit from more than one parent class.

class engine:
    def start_engine(self):
        print("engine started")
    def stop_engine(self):
        print("engine stopped")
class body:
    def open_door(self):
        print("door opened")
    def close_door(self):
        print("door closed")
class car(engine,body):
    def drive(self):
        print("car is in motion")
    def park(self):
        print("car is parked")

my_car = car()
my_car.start_engine()
my_car.stop_engine()
my_car.open_door()
my_car.close_door()
my_car.drive()
my_car.park()