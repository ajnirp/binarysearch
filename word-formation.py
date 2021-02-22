# https://binarysearch.com/problems/Word-Formation

from collections import Counter

class Solution:
    def solve(self, words, letters):
        lc = Counter(letters)
        max_len = 0
        for word in words:
            wc = Counter(word)
            if all(k in lc and lc[k] >= wc[k] for k in wc):
                max_len = max(max_len, len(word))
        return max_len