# butterfly pattern
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print('*', end="")
#     for j in range(1, 2 * (5 - i)):
#         print('', end="")
#     for j in range(1, i + 1):
#         print('*', end="") 
#     print()       

#Hollow number pyramid
for i in range(1, 6):
    for j in range(1, 6 - i):
        print('', end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(i, end='')    
        else:
            print('', end="")
    print()        