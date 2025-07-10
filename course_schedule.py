def can_finish(numCourses, prerequisites):
    from collections import defaultdict
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    visited = set()
    path = set()

    def dfs(course):
        if course in path:
            return False
        if course in visited:
            return True
        path.add(course)
        for pre in graph[course]:
            if not dfs(pre):
                return False
        path.remove(course)
        visited.add(course)
        return True

    return all(dfs(c) for c in range(numCourses))

print(can_finish(2, [[1,0]]))  # True
