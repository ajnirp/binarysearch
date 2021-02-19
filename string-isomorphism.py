# https://binarysearch.com/problems/String-Isomorphism

class Solution:
    def solve(self, s, t):
        if len(s) != len(t):
            return False
        forward = {}
        for c, d in zip(s, t):
            if c not in forward:
                forward[c] = d
            else:
                if forward[c] != d:
                    return False
        reverse = {}
        for c in forward:
            d = forward[c]
            if d not in reverse:
                reverse[d] = c
            else:
                if reverse[d] != c:
                    return False
        return True