# https://binarysearch.com/problems/Substringify

class Solution:
    def solve(self, s, t):
        if len(s) == 0:
            return 0
        m, n = len(t), len(s)
        result = 1e10
        for i in range(n-m+1):
            result = min(result, sum(t[j] != s[i+j] for j in range(m)))
        return result