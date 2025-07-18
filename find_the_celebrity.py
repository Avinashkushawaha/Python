def find_celebrity(n, knows):
    def is_celebrity(c):
        for i in range(n):
            if i != c and (knows(c, i) or not knows(i, c)):
                return False
        return True

    celeb = 0
    for i in range(1, n):
        if knows(celeb, i):
            celeb = i
    return celeb if is_celebrity(celeb) else -1
