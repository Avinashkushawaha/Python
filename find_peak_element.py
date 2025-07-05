def find_peak_grid(mat):
    rows, cols = len(mat), len(mat[0])
    l, r = 0, cols - 1

    while l <= r:
        mid = (l + r) // 2
        max_row = max(range(rows), key=lambda x: mat[x][mid])
        if (mid == 0 or mat[max_row][mid] > mat[max_row][mid - 1]) and \
           (mid == cols - 1 or mat[max_row][mid] > mat[max_row][mid + 1]):
            return [max_row, mid]
        elif mid > 0 and mat[max_row][mid - 1] > mat[max_row][mid]:
            r = mid - 1
        else:
            l = mid + 1
