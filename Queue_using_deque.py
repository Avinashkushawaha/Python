from collections import deque

queue = deque()

queue.append(10)
queue.append(20)

print(queue.popleft())
print(queue.popleft())