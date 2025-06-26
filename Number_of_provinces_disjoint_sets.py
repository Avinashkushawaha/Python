def find_provinces(is_connected):
    def dfs(node):
        visited.add(node)
        for nei in range(len(is_connected)):
            if is_connected[node][nei] and nei not in visited:
                dfs(nei)

    visited = set()
    count = 0
    for i in range(len(is_connected)):
        if i not in visited:
            dfs(i)
            count += 1
    return count

matrix = [[1,1,0],[1,1,0],[0,0,1]]
print(find_provinces(matrix))  # 2
