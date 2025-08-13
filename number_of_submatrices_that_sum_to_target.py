from collections import defaultdict

def numSubmatrixSumTarget(matrix, target):
    n, m = len(matrix), len(matrix[0])
    for row in matrix:
        for j in range(1, m):
            row[j] += row[j-1]
    count = 0
    for c1 in range(m):
        for c2 in range(c1, m):
            sums = defaultdict(int)
            sums[0] = 1
            curSum = 0
            for r in range(n):
                curSum += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                count += sums[curSum - target]
                sums[curSum] += 1
    return count

print(numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))
