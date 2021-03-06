# https://binarysearch.com/problems/Compress-String

class Solution:
    def solve(self, s):
        last_seen = None
        result = []
        for c in s:
            if c == last_seen:
                continue
            result.append(c)
            last_seen = c
        return ''.join(result)