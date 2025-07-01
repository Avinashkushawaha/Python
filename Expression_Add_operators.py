def add_operators(num, target):
    res = []

    def backtrack(index, path, value, prev):
        if index == len(num):
            if value == target:
                res.append(path)
            return
        for i in range(index+1, len(num)+1):
            temp = num[index:i]
            if len(temp) > 1 and temp[0] == '0': break
            n = int(temp)
            if index == 0:
                backtrack(i, temp, n, n)
            else:
                backtrack(i, path + '+' + temp, value + n, n)
                backtrack(i, path + '-' + temp, value - n, -n)
                backtrack(i, path + '*' + temp, value - prev + prev * n, prev * n)

    backtrack(0, "", 0, 0)
    return res

print(add_operators("123", 6))  # ['1+2+3', '1*2*3']
