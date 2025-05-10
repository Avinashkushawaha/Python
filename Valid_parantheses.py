def is_valid(s):
    stack = []
    pair = {')':'(',']':'[','}':'{'}
    for char in s:
        if char in pair.values():
            stack.append(char)
        elif stack and stack[-1] == pair[char]:
            stack.pop()
        else:
            return False

    return not stack            