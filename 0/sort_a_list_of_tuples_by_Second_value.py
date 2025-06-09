def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[1])

print(sort_tuples([(1, 3), (2, 1), (4, 2)]))