def maxPerformance(n, speed, efficiency, k):
    workers = sorted(zip(efficiency, speed), reverse=True)
    import heapq
    heap, speed_sum, res = [], 0, 0

    for e, s in workers:
        heapq.heappush(heap, s)
        speed_sum += s
        if len(heap) > k:
            speed_sum -= heapq.heappop(heap)
        res = max(res, speed_sum * e)
    return res % (10**9 + 7)

print(maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))
