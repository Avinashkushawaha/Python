def find_circle_num(isConnected):
    n = len(isConnected)
    visited = set()

    def dfs(i):
        for j in range(n):
            if isConnected[i][j] == 1 and j not in visited:
                visited.add(j)
                dfs(j)

    count = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1
    return count
