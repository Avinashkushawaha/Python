from collections import Counter 

def sort_by_frequency(arr):
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))

print(sort_by_frequency([4, 5, 6, 5, 4,3]))