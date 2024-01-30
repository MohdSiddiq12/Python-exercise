# Creating a dictionary
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values
print(person['name'])
print(person.get('age', 'N/A'))  # Using get() to handle key absence

# Modifying values
person['age'] = 31

# Adding a new key-value pair
person['occupation'] = 'Engineer'

# Iterating over keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Creating a set
fruits = {'apple', 'banana', 'orange'}

# Adding and removing elements
fruits.add('grape')
fruits.remove('banana')

# Checking membership
print('apple' in fruits)  

# Set operations (union, intersection, difference)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

print(f"Union: {union_set}")   
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")

