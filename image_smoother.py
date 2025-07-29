def imageSmoother(img):
    rows, cols = len(img), len(img[0])
    res = [[0]*cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            total = count = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if 0 <= i < rows and 0 <= j < cols:
                        total += img[i][j]
                        count += 1
            res[r][c] = total // count
    return res
