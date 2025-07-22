def fractionToDecimal(numerator, denominator):
    if numerator == 0: return "0"
    res = '-' if (numerator < 0) ^ (denominator < 0) else ''
    numerator, denominator = abs(numerator), abs(denominator)
    res += str(numerator // denominator)
    rem = numerator % denominator
    if rem == 0:
        return res
    res += '.'
    rem_map = {}
    while rem:
        if rem in rem_map:
            idx = rem_map[rem]
            return res[:idx] + '(' + res[idx:] + ')'
        rem_map[rem] = len(res)
        rem *= 10
        res += str(rem // denominator)
        rem %= denominator
    return res
