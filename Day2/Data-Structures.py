# # # Topics to Cover
# # # Lists
# # # Tuples
# # # Dictionaries
# # # Sets

# # # Create a List:
# # # Write a Python program to create a list of your favorite movies and print each movie.

# # movies = ['slumdog millionare','inception','dark knight rises','Batman','The pursuit of happiness']
# # # for i in movies:
# # #     print(i)

# # # List Operations:
# # # Write a Python program to perform the following operations on a list:

# # # Append a new item.


# # movies.append('interstellar')


# # # Remove an item.

# # movies.remove('slumdog millionare')



# # # Sort the list.

# # movies.sort()

# # # Reverse the list.

# # movies.reverse()

# # # Print the length of the list.

# # # for i in movies:
# # #     print(len(i))

# #  #list slicing
# # print(movies[:3])
# # print(movies[-3:])
    

# # Create a Tuple:
# # Write a Python program to create a tuple of your favorite books and print each book.

# books = ('Negogiating as your life depends on it','leadership qualities','the subtle art of not giving a fuck')
# # for i in books:
# #     print(i)

# # Tuple Operations:
# # Write a Python program to:

# # Convert the tuple to a list.

# books = list(books)
# # print(books)
# # Add a new book to the list.

# books.append('rich dad poor dad')
# # print(books)
# # Convert the list back to a tuple.

# books = tuple(books)
# # print(books)
# # Print the final tuple.

# # print(books)

# # Access Tuple Elements:
# print(books[-3])


# Create a Dictionary Create a Dictionary:
# Write a Python program to create a dictionary with keys as the names of your friends and values as their phone numbers. Print each friend's name and phone number.
dict = {'sid':7674,'john':1234,'ajay':3456}
for name,phone in dict.items():
    print('name',name + 'phone', + phone)