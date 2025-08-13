from collections import Counter

def leastInterval(tasks, n):
    freq = list(Counter(tasks).values())
    maxFreq = max(freq)
    maxCount = freq.count(maxFreq)
    return max(len(tasks), (maxFreq-1)*(n+1) + maxCount)

print(leastInterval(["A","A","A","B","B","B"], 2))
