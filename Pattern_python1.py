# Right angle triangle number pattern
# for i in range(1, 6):
#     print(''.join(str(x)for x in range(1, i + 1)))

#Inverted right angle traingle number pattern 
# for i in range(5,0, -1):
#     print(''.join(str(x)for x in range(1, i + 1)))

# floyd's triangle
# num  = 1 
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(num, end="")
#         num +=1
#     print()    

# hollow right angle triangle
# for i in  range(1, 5):
#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == 5:
#             print('*', end="")
#         else:
#             print('', end="")
#     print()            

# hollow pyramid pattern
# for i in range(1, 6):
#     for j in range(5 -i):
#         print('', end="")
#         for j in range(2 * i - 1):
#             if j == 0 or j == 2 * i - 2 or i == 5:
#                 print('*', end="")
#             else:
#                 print('', end="")
#         print()            

# hollow diamond pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print('', end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(i, end="")
        else:
            print('', end="")
    print()                