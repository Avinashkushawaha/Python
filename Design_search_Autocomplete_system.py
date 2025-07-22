from collections import defaultdict
import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.curr = self.root
        self.prefix = ''
        for s, t in zip(sentences, times):
            self.insert(s, t)

    def insert(self, s, t):
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.sentences[s] += t

    def input(self, c):
        if c == '#':
            self.insert(self.prefix, 1)
            self.prefix = ''
            self.curr = self.root
            return []
        self.prefix += c
        if c not in self.curr.children:
            self.curr = TrieNode()
            return []
        self.curr = self.curr.children[c]
        heap = [(-freq, s) for s, freq in self.curr.sentences.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(min(3, len(heap)))]
