def minFlipsMonoIncr(s):
    one_count = flips = 0
    for ch in s:
        if ch == '1':
            one_count += 1
        else:
            flips = min(flips + 1, one_count)
    return flips
