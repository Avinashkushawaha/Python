def decode_string(s):
    stack, curr_num, curr_str = [], 0, ''
    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c == '[':
            stack.append((curr_str, curr_num))
            curr_str, curr_num = '', 0
        elif c == ']':
            last_str, num = stack.pop()
            curr_str = last_str + num * curr_str
        else:
            curr_str += c
    return curr_str

print(decode_string("3[a2[c]]"))  # accaccacc
