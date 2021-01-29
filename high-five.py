# https://binarysearch.com/problems/High-Five

# to make a number as small as possible, put 5 to the left of the first digit from the left that's > 5

# to make a number as large as possible, put a 5 at the left of the first digit from the left that's < 5

class Solution:
    def split(self, n):
        return [c for c in str(n)]

    def make_smallest(self, n):
        s = self.split(n)
        for i in range(len(s)):
            if s[i] > '5':
                return s[:i] + ['5'] + s[i:]
        return s + ['5']

    def make_largest(self, n):
        s = self.split(n)
        for i in range(len(s)):
            if s[i] < '5':
                return s[:i] + ['5'] + s[i:]
        return s + ['5']

    def solve(self, n):
        result = self.make_largest(n) if n >= 0 else self.make_smallest(-n)
        result = int(''.join(result))
        if n < 0:
            result = -result
        return result