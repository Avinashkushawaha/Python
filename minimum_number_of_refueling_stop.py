import heapq

def minRefuelStops(target, startFuel, stations):
    maxHeap = []
    fuel = startFuel
    i = stops = 0
    while fuel < target:
        while i < len(stations) and stations[i][0] <= fuel:
            heapq.heappush(maxHeap, -stations[i][1])
            i += 1
        if not maxHeap:
            return -1
        fuel += -heapq.heappop(maxHeap)
        stops += 1
    return stops

print(minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]]))
