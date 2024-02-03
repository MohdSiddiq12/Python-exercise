# # Common Built-in Functions

# # len() - Returns the length of an object (e.g., string, list, tuple)
# my_string = "Hello, Python!"
# length = len(my_string)
# print("Length:", length)

# # type() - Returns the type of an object
# print("Type of my_string:", type(my_string))

# # int(), float(), str() - Type conversion functions
# num_str = "42"
# num_int = int(num_str)
# print("Converted to int:", num_int)

# # max() and min() - Returns the maximum and minimum values in an iterable
# numbers = [3, 7, 1, 9, 4]
# max_value = max(numbers)
# min_value = min(numbers)
# print("Max:", max_value, "| Min:", min_value)

# # sorted() - Returns a sorted list from the elements of an iterable
# sorted_numbers = sorted(numbers)
# print("Sorted numbers:", sorted_numbers)

# # sum() - Returns the sum of elements in an iterable
# sum_of_numbers = sum(numbers)
# print("Sum of numbers:", sum_of_numbers)

#more intermediate built in functions 


# map() - Applies a function to all items in an input list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)
