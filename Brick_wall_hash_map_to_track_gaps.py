from collections import defaultdict

def leastBricks(wall):
    counter = defaultdict(int)
    for row in wall:
        total = 0
        for brick in row[:-1]:
            total += brick
            counter[total] += 1
    return len(wall) - max(counter.values(), default=0)
