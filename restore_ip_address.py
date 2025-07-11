def restore_ip_addresses(s):
    res = []
    def backtrack(start, parts):
        if start == len(s) and len(parts) == 4:
            res.append('.'.join(parts))
            return
        if len(parts) >= 4:
            return
        for l in range(1, 4):
            if start + l > len(s): break
            part = s[start:start+l]
            if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                continue
            backtrack(start+l, parts + [part])
    backtrack(0, [])
    return res

print(restore_ip_addresses("25525511135"))
