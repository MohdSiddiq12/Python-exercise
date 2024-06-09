# For Day 8, let's focus on mastering Python libraries for data analysis and visualization.
# Specifically, we'll work with NumPy, Pandas, and Matplotlib, which are essential for data manipulation, 
# analysis, and visualization.

# Topics to Cover
# NumPy: Understanding arrays and basic operations
# Pandas: DataFrames, data manipulation, and analysis
# Matplotlib: Data visualization
# Learning Objectives
# Understand how to create and manipulate NumPy arrays.
# Learn how to use Pandas for data manipulation and analysis.
# Understand how to create basic plots using Matplotlib.

# Create a NumPy Array:
# Write a Python program to create a NumPy array of 10 zeros, 10 ones, and 10 fives.
import numpy as np

# # Create arrays of zeros, ones, and fives
# zeros = np.zeros(10)
# ones = np.ones(10) * 2
# fives = np.ones(10) * 5

# print("Zeros:", zeros)
# print("Ones:", ones)
# print("Fives:", fives)


# Array Operations:
# Write a Python program to create a NumPy array of integers from 1 to 20. Reshape the array to 4x5 and calculate the sum of each column
# arr = np.arange(1,21)
# reshaped_arr = arr.reshape(4, 5)

# col = reshaped_arr.sum(axis=0)
# print("reshaped_array: ",reshaped_arr)
# print(col)

# Create a DataFrame:
# Write a Python program to create a Pandas DataFrame from a dictionary of lists. Print the DataFrame.

# import pandas as pd

# # Create a dictionary of lists
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [24, 27, 22, 32],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# print("DataFrame:\n", df)

# filtered = df[df['Age'] > 22]
# print(filtered)

# Matplotlib
# Basic Plot:
# Write a Python program to create a simple line plot using Matplotlib. Plot the values of y = x^2 for x in the range 0 to 10.

import matplotlib.pyplot as plt

# Create data
# x = range(0, 11)
# y = [i**2 for i in x]

# # Create a line plot
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y = x^2')
# plt.title('Line Plot of y = x^2')
# plt.show()

# Bar Plot:
# Write a Python program to create a bar plot using Matplotlib from a given set of data.
import matplotlib.pyplot as plt

# Data for the bar plot
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

# Create a bar plot
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
plt.show()

