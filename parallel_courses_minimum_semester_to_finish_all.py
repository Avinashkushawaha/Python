from collections import deque, defaultdict

def minimumSemesters(n, relations):
    graph = defaultdict(list)
    indegree = [0] * (n+1)
    for u, v in relations:
        graph[u].append(v)
        indegree[v] += 1
    q = deque([i for i in range(1, n+1) if indegree[i] == 0])
    semester = 0
    taken = 0
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            taken += 1
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        semester += 1
    return semester if taken == n else -1

print(minimumSemesters(3, [[1,3],[2,3]]))
