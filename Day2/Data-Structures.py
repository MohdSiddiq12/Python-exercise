# Topics to Cover
# Lists
# Tuples
# Dictionaries
# Sets

# Create a List:
# Write a Python program to create a list of your favorite movies and print each movie.

movies = ['slumdog millionare','inception','dark knight rises','Batman','The pursuit of happiness']
for i in movies:
    print(i)

# List Operations:
#Write a Python program to perform the following operations on a list:

movies.append('interstellar') # Append a new item.

movies.remove('slumdog millionare') # Remove an item.

movies.sort() #sort the list

movies.reverse() #reverse the list

print(movies[:3])   #list slicing

print(movies[-3:])   #list slicing

# Print the length of the list.

for i in movies:
    print(len(i))


    

# Create a Tuple:
# Write a Python program to create a tuple of your favorite books and print each book.

books = ('Negogiating as your life depends on it','leadership qualities','the subtle art of not giving a fuck')
for i in books:
    print(i)

#Tuple Operations:
#Write a Python program to:

#Convert the tuple to a list.
#because tuple is immutable we convert it to list
books = list(books)
print(books)

books.append('rich dad poor dad') #Add a new book to the list.
print(books)

books = tuple(books) #Convert the list back to a tuple.
print(books)

#Print the final tuple.
print(books)

print(books[-3]) #Access Tuple Elements:



#Create a Dictionary Create a Dictionary:
#Write a Python program to create a dictionary with keys as the names of your friends and values as their phone numbers. Print each friend's name and phone number.
dict = {'sid':7674,'john':1234,'ajay':3456}


#Dictionary Operations:
#Write a Python program to: Add a new friend and phone number.

dict['joe'] = 9876



dict['joe'] = 7890 # Update an existing phone number.


for name,phone in dict.items():
    print('name',name  +  'phone', + phone)

del dict['john'] #Remove a friend from the dictionary.
for name,phone in dict.items():
    print('name',name  +  'phone', + phone)
#Print the dictionary.


#sets
fruits = {"apple", "banana", "cherry", "date", "elderberry"}
for fruit in fruits:
    print(fruit)

#set operations

# Write a Python program to perform the following operations on two sets of fruits:

# Find the union of the sets.
fruits1 = {'apple','banana','mango','date'}
fruits2 = {'cherry','date','elderberry'}
print(fruits1.union(fruits2))

# Find the intersection of the sets.
print(fruits1.intersection(fruits2))

# Find the difference between the sets.
print(fruits1.difference(fruits2))
print(fruits2.difference(fruits1))
# Check if one set is a subset of the other.

print(fruits1.issubset(fruits2))

# Summary of Differences
# Lists: Mutable, ordered, allows duplicates, defined with [].
# Tuples: Immutable, ordered, allows duplicates, defined with ().
# Dictionaries: Mutable, unordered, unique keys, allows duplicate values, defined with {key: value}.
# Sets: Mutable, unordered, unique elements, defined with {} or set()
