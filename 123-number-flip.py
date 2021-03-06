# https://binarysearch.com/problems/123-Number-Flip

# flip the first non-3 digit you see

class Solution:
    def solve(self, n):
        s = str(n)
        res = []
        flipped = False
        for c in s:
            if c != '3':
                if flipped:
                    res.append(c)
                else:
                    res.append('3')
                    flipped = True
            else:
                res.append(c)
        return int(''.join(res))
