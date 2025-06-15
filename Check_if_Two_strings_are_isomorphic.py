def is_ismorphic(s1, s2):
    if len(s1) != len(s2):
        return False 
    map1, map2 = {}, {}
    for c1, c2 in zip(s1, s2):
        if map1.get(c1, c2) != c2 or map2.get(c2, c1) != c1:
            return False
        map1[c1] = c2
        map2[c2] = c1
    return True

print(is_ismorphic("egg", "add"))  
print(is_ismorphic("foo", "bar"))  
