import bisect

def find_radius(houses, heaters):
    heaters.sort()
    res = 0
    for house in houses:
        i = bisect.bisect_left(heaters, house)
        left = float('inf') if i == 0 else house - heaters[i - 1]
        right = float('inf') if i == len(heaters) else heaters[i] - house
        res = max(res, min(left, right))
    return res
