from collections import Counter

def count_occurrences(lst):
    return dict(Counter(lst))

print(count_occurrences(['apple', 'banana', 'apple', 'orange', 'banana']))
# {'apple': 2, 'banana': 2, 'orange': 1}
