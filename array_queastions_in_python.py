# how many subarrays present in an array

# arr = [1, 2, 3]
# target = 3
# def find_index(arr, target):
#     for index, value in enumerate(arr):
#         if value == target:
#             return index
#     return -1
# print(find_index(arr, target))

# arr = [1, 2, 3]
# target = 3

# for index, value in enumerate(arr):
#     if value == target:
#         print(index)
    

arr = [1,1, 2, 3, 4, 5]
target = 3

for index, value in enumerate(arr):
    if value == target:
        print(index)
    