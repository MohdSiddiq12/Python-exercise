# Iterate over a list
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# Using range to iterate over numbers
for num in range(1, 5):
    print(num)

# Simple while loop
counter = 0
while counter < 5:
    print(f"Count: {counter}")
    counter += 1

# Break statement
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue statement
for j in range(5):
    if j == 2:
        continue
    print(j)

# Nested loops
for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")


# For loop with else block
for i in range(5):
    print(i)
else:
    print("Loop completed!")

# While loop with else block
counter = 0
while counter < 3:
    print(f"Count: {counter}")
    counter += 1
else:
    print(f"While loop completed!")

