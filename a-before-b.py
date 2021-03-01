# https://binarysearch.com/problems/As-Before-Bs

# INCOMPLETE: i'm only deleting A's

class Solution:
    def solve(self, s):
        first_b = -1
        for i in range(0, len(s)):
            if s[i] == 'B':
                first_b = i
                break
        if first_b == -1:
            return 0
        return sum(s[k] == 'A' for k in range(first_b+1, len(s)))