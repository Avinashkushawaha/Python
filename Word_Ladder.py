from collections import deque

def ladder_length(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    q = deque([(beginWord, 1)])
    while q:
        word, length = q.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new = word[:i] + c + word[i+1:]
                if new in word_set:
                    word_set.remove(new)
                    q.append((new, length + 1))
    return 0
