def arrange_coins(n):
    l, r = 0, n
    while l <= r:
        mid = (l + r) // 2
        total = mid * (mid + 1) // 2
        if total == n:
            return mid
        elif total < n:
            l = mid + 1
        else:
            r = mid - 1
    return r
