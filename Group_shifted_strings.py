from collections import defaultdict

def group_shifted(strings):
    def shift_key(s):
        base = ord(s[0])
        return tuple((ord(c) - base) % 26 for c in s)
    
    groups = defaultdict(list)
    for word in strings:
        groups[shift_key(word)].append(word)
    return list(groups.values())
