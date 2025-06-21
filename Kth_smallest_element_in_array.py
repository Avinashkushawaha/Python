import heapq

def kth_smallest(arr, k):
    return heapq.nsmallest(k, arr)[-1]

print(kth_smallest([7, 10, 4, 3, 20, 15], 3))  # Output: 7