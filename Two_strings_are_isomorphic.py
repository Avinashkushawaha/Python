def is_isomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

print(is_isomorphic("egg", "add"))  # True
print(is_isomorphic("foo", "bar"))  # False
