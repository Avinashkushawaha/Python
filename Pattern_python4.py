# Pascal's triangle
# import math
# n = 5
# for i in range(n):
#     for j in range(n - i - 1):
#         print('', end="")
#         for j in range(i + 1):
#             print(str(math.comb(i, j))+ '', end="")
#         print()    


# zig zag pattern
for i in range(1, 6):
    if i % 2 == 0:
        print(''* (i - 1) + '*')
    else:
        print('*' * i)    