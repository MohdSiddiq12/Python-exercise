
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
# data = {
#     'name': ['bob','marley','roca','zendaya'],
#     'age': [17,22,35,23],
#     'city': ['nyc','hyderabad','paris','london'],
#     'salary': [18000,20000,22000,35000]
# }

# df = pd.DataFrame(data)
# filtered = df[['name','age','salary']][df['age']>17]
# print(filtered)

# Sorting:
# Write a Python program to sort a DataFrame by multiple columns.

# data = {
#     'name': ['bob','marley','roca','zendaya','hill','jack','mike'],
#     'age': [17,22,35,23,21,20,20],
#     'city': ['nyc','hyderabad','paris','london','istanbul','sogut','zech'],
#     'salary': [18000,20000,22000,35000,70000,11000,88000]
# }

# df = pd.DataFrame(data)
# sorting = df.sort_values(by=['age','salary'],ascending=[True,False])
# print(sorting)

# Merge DataFrames:
# Write a Python program to merge two DataFrames based on a common column.

# df1 = pd.DataFrame({
#     'ID': [1,2,3],
#     'Name': ['Joe','rachel','chandler']
# })

# df2 = pd.DataFrame({
#     'ID': [2,3,4],
#     'Name': ['rachel','chandler','Monica']
# })

# merged = pd.merge(df1, df2, on='ID', how='inner')
# print("merged dataset \n",merged)

# Join DataFrames:
# Write a Python program to perform different types of joins (inner, outer, left, right) on two DataFrames.
import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Age': [22, 32, 29, 24]
})

# Set 'ID' as the index
df1.set_index('ID', inplace=True)
df2.set_index('ID', inplace=True)

# Perform different types of joins
inner_join = df1.join(df2, how='inner')
outer_join = df1.join(df2, how='outer')
left_join = df1.join(df2, how='left')
right_join = df1.join(df2, how='right')

print("Inner Join:\n", inner_join)
print("Outer Join:\n", outer_join)
print("Left Join:\n", left_join)
print("Right Join:\n", right_join)
