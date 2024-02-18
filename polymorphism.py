# Base class
class Animal:
    def speak(self):
        pass

# Subclasses demonstrating polymorphism
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Function demonstrating polymorphism
def animal_sound(animal):
    return animal.speak()

# Creating instances of subclasses
my_dog = Dog()
my_cat = Cat()
my_duck = Duck()

# Calling the function with different objects
print(animal_sound(my_dog))  # Output: Woof!
print(animal_sound(my_cat))  # Output: Meow!
print(animal_sound(my_duck)) # Output: Quack!
