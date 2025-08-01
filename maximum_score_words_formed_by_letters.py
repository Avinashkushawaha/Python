class Solution:
    def maxScoreWords(self, words, letters, score):
        from collections import Counter
        
        letter_count = Counter(letters)

        def dfs(i, curr_score, curr_count):
            if i == len(words):
                return curr_score
            res = dfs(i+1, curr_score, curr_count.copy())  # skip word
            word_count = Counter(words[i])
            if all(curr_count[c] >= word_count[c] for c in word_count):
                for c in word_count:
                    curr_count[c] -= word_count[c]
                word_score = sum(score[ord(c) - ord('a')] * word_count[c] for c in word_count)
                res = max(res, dfs(i+1, curr_score + word_score, curr_count))
            return res

        return dfs(0, 0, letter_count)
