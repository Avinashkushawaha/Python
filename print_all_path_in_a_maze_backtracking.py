def find_path(maze, x, y, path, visited):
    n = len(maze)
    if x == n-1 and y == n-1:
        print(path)
        return 
    for dx, dy, move in [(1, 0, 'D'), (0, 1, 'R'), (-1, 0, 'U'), (0, -1, 'L')]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < n and 0 <= new_y < n and maze[new_x][new_y] == 1 and not visited[new_x][new_y]:
            visited[new_x][new_y] = True
            find_path(maze, new_x, new_y, path + move, visited)
            visited[new_x][new_y] = False

maze = [[1, 0, 0], [1, 1, 0], [0, 1, 1]]
visited = [[False]*3 for _ in range(3)] 
visited[0][0] = True
find_path(maze, 0, 0, '', visited)            