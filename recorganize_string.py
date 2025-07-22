from collections import Counter
import heapq

def reorganizeString(s):
    counter = Counter(s)
    max_heap = [(-cnt, char) for char, cnt in counter.items()]
    heapq.heapify(max_heap)
    res = []

    prev = (0, '')
    while max_heap:
        cnt, char = heapq.heappop(max_heap)
        res.append(char)
        if prev[0] < 0:
            heapq.heappush(max_heap, prev)
        prev = (cnt + 1, char)
    
    res = ''.join(res)
    return res if len(res) == len(s) else ''
