def min_cost(nums, cost):
    pairs = sorted(zip(nums, cost))
    total = sum(cost)
    mid = total // 2
    acc = 0
    for num, c in pairs:
        acc += c
        if acc > mid:
            target = num
            break
    return sum(abs(n - target) * c for n, c in zip(nums, cost))
