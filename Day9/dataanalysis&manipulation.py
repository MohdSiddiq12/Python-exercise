
# For Day 9, let's focus on advanced data analysis and manipulation using Pandas. 
# This will include more complex operations such as merging, grouping, pivoting, and handling missing data.

# Topics to Cover
# Advanced DataFrame operations
# Merging and joining DataFrames
# Grouping and aggregation
# Pivot tables
# Handling missing data
# Learning Objectives
# Understand how to perform advanced DataFrame manipulations.
# Learn how to merge and join DataFrames.
# Understand grouping and aggregation for data analysis.
# Learn how to create and manipulate pivot tables.
# Understand techniques for handling missing data in DataFrames

# Selecting and Filtering:
# Write a Python program to select specific columns and filter rows based on a condition in a DataFrame.
import pandas as pd
data = {
    'name': ['bob','marley','roca','zendaya'],
    'age': [17,22,35,23],
    'city': ['nyc','hyderabad','paris','london'],
    'salary': [18000,20000,22000,35000]
}

df = pd.DataFrame(data)
filtered = df[['name','age','salary']][df['age']>17]
print(filtered)

