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
arr = np.arange(1,21)
reshaped_arr = arr.reshape(4, 5)

col = reshaped_arr.sum(axis=0)
print("reshaped_array: ",reshaped_arr)
print(col)