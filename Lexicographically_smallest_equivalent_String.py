def smallestEquivalentString(s1, s2, baseStr):
    parent = list(range(26))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for a, b in zip(s1, s2):
        pa, pb = find(ord(a)-97), find(ord(b)-97)
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

    return ''.join(chr(find(ord(c)-97)+97) for c in baseStr)
