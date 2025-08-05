from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val):
        self.freq[val] += 1
        f = self.freq[val]
        self.group[f].append(val)
        self.maxFreq = max(self.maxFreq, f)

    def pop(self):
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return val
