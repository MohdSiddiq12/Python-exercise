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
