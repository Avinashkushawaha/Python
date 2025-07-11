class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = True

    def search(self, word):
        def dfs(j, node):
            for i in range(j, len(word)):
                if word[i] == '.':
                    return any(dfs(i+1, node[k]) for k in node if k != '$')
                if word[i] not in node:
                    return False
                node = node[word[i]]
            return '$' in node
        return dfs(0, self.trie)
