import heapq

def min_meeting_rooms(intervals):
    if not intervals: return 0
    intervals.sort()
    heap = [intervals[0][1]]
    for start, end in intervals[1:]:
        if start >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)

print(min_meeting_rooms([[0, 30],[5, 10],[15, 20]]))  # 2
