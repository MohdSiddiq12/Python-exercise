
# Great! For Day 5, let's focus on mastering file handling in Python. This includes reading from and writing to files,
#  which is an essential skill for many programming tasks such as data processing, logging, and configuration management.

# Topics to Cover
# Reading from files
# Writing to files
# Appending to files
# Working with different file modes
# Context managers (with statement)
# Learning Objectives
# Understand how to open and close files.
# Learn how to read from files using different methods.
# Learn how to write to files and append data to files.
# Understand the importance of using context managers to handle files efficiently.

# Read Entire File:
# Write a Python program to read the entire contents of a text file and print them to the console.

with open('Day5\example.txt','r') as file:
    content = file.read()
    print(content)

# Read File Line by Line:
# Write a Python program to read a file line by line and print each line to the console.

with open('Day5\example.txt','r') as file:
    content = file.read()
    print(content, end=" ")

# Writing to Files
# Write to a File:
# Write a Python program to write a list of strings to a file, each string on a new line.
