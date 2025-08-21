def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    map_s, map_t = {}, {}
    for c1, c2 in zip(s, t):
        if map_s.get(c1, c2) != c2 or map_t.get(c2, c1) != c1:
            return False
        map_s[c1] = c2
        map_t[c2] = c1
    return True

print(isIsomorphic("egg", "add"))  # True
print(isIsomorphic("foo", "bar"))  # False
