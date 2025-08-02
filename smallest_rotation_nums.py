def bestRotation(nums):
    n = len(nums)
    change = [0]*n
    for i, num in enumerate(nums):
        change[(i - num + 1) % n] -= 1
    score = 0
    max_score = 0
    best_k = 0
    for i in range(1, n):
        score += 1 + change[i]
        if score > max_score:
            max_score = score
            best_k = i
    return best_k
