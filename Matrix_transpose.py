def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

matrix = [[1, 2], [3, 4], [5, 6]]
print(transpose(matrix))  # [[1, 3, 5], [2, 4, 6]]
