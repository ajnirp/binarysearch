# https://binarysearch.com/problems/String-Sequence

class Solution:
    def helper(self, s0, s1, n):
        if n == 0:
            return s0
        if n == 1:
            return s1
        if n not in self.dp:
            if n & 1 == 0:
                self.dp[n] = self.helper(s0, s1, n-1) + self.helper(s0, s1, n-2)
            else:
                self.dp[n] = self.helper(s0, s1, n-2) + self.helper(s0, s1, n-1)
        return self.dp[n]

    def solve(self, s0, s1, n):
        self.dp = {}
        return self.helper(s0, s1, n)