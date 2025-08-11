import heapq
def smallestRange(nums):
    heap = []
    max_val = float('-inf')
    for i, arr in enumerate(nums):
        heapq.heappush(heap, (arr[0], i, 0))
        max_val = max(max_val, arr[0])
    
    res = [float('-inf'), float('inf')]
    while heap:
        min_val, r, c = heapq.heappop(heap)
        if max_val - min_val < res[1] - res[0]:
            res = [min_val, max_val]
        if c + 1 == len(nums[r]):
            break
        nxt = nums[r][c+1]
        heapq.heappush(heap, (nxt, r, c+1))
        max_val = max(max_val, nxt)
    return res

print(smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
