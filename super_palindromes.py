def superpalindromesInRange(left, right):
    l, r = int(left), int(right)
    count = 0
    
    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    for k in range(1, 100000):
        s = str(k)
        t = int(s + s[::-1])
        square = t * t
        if square > r:
            break
        if square >= l and is_palindrome(square):
            count += 1

    for k in range(1, 100000):
        s = str(k)
        t = int(s + s[-2::-1])
        square = t * t
        if square > r:
            break
        if square >= l and is_palindrome(square):
            count += 1

    return count
