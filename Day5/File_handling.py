
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

# with open('Day5\example.txt','r') as file:
#     content = file.read()
#     print(content)

# Read File Line by Line:
# Write a Python program to read a file line by line and print each line to the console.

# with open('Day5\example.txt','r') as file:
#     content = file.read()
#     print(content, end=" ")

# Writing to Files
# Write to a File:
# Write a Python program to write a list of strings to a file, each string on a new line.

# lines = ['hello ', 'siddiq']
# with open('Day5\example.txt','w') as file:
#     for line in lines:
#         file.write(line + '\n')


# Appending to Files
# Append to a File:
# Write a Python program to append a list of strings to an existing file.

# lines = ['how are ','you']
# with open('Day5\example.txt','a') as file:
#     for line in lines:
#         file.write(line + '\n')

# Using Context Managers
# Context Manager for File Operations:
# Write a Python program that reads a file and writes its content to another file using a context manager.

with open('Day5\example.txt','r') as source:
    with open('Day5\destination.txt','w') as destination:
        for line in source:
            destination.write(line + '\n')