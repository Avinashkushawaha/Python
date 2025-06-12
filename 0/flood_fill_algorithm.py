def flood_fill(image, sr, sc, new_color):
    orig = image[sr][sc]
    if orig == new_color:
        return image
    
    def dfs(r, c):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != orig:
            return
        
        image[r][c] = new_color
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image

img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(flood_fill(img, 1, 1, 2))

    

