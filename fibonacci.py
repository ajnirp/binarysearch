# https://binarysearch.com/problems/A-Flight-of-Stairs

class Solution:
    def solve(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return b % 1000000007

print(Solution().solve(4)) # expected: 5