def ship_within_days(weights, D):
    def can_ship(cap):
        days = 1
        curr = 0
        for w in weights:
            if curr + w > cap:
                days += 1
                curr = 0
            curr += w
        return days <= D

    l, r = max(weights), sum(weights)
    while l < r:
        mid = (l + r) // 2
        if can_ship(mid):
            r = mid
        else:
            l = mid + 1
    return l
