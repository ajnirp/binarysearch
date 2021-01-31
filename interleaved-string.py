# https://binarysearch.com/problems/Interleaved-String

class Solution:
    def solve(self, s0, s1):
        ans = []
        for c1, c2 in zip(s0, s1):
            ans.append(c1)
            ans.append(c2)
        # one of the last two terms will be the empty string, the other one
        # will contain all the leftover chars
        return ''.join(ans) + s0[len(s1):] + s1[len(s0):]