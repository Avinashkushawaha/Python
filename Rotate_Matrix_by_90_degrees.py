def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]    
rotate(mat)
print(mat)  # Output: [[7, 4, 1], [8,            