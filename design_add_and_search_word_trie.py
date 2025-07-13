class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['#'] = True

    def search(self, word):
        def dfs(i, node):
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    return any(dfs(j + 1, node[k]) for k in node if k != '#')
                if c not in node:
                    return False
                node = node[c]
            return '#' in node
        return dfs(0, self.trie)
