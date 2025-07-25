def powerfulIntegers(x, y, bound):
    res = set()
    i = 1
    while i < bound:
        j = 1
        while i + j <= bound:
            res.add(i + j)
            if y == 1: break
            j *= y
        if x == 1: break
        i *= x
    return list(res)
