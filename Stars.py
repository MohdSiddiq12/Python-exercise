# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end= " ")
#     print()

# n = 4
# for i in range(n):
#     for j in range(i,n):
#         print("*",end= " ")
#     print()

#star pattern 

n = 6 
for i in  range(n):
    for j in range(i,n):
        print(" ",end= " ")

    for j in range(i+1):
        print("*",end=" ")
    print()
