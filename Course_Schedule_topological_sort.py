from collections import defaultdict, deque

def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    indegree = [0]*num_courses
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1

    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return count == num_courses

print(can_finish(2, [[1,0]]))  # True
