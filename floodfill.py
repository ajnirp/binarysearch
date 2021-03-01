# https://binarysearch.com/problems/Paint-Bucket

class Solution:
    def bounds(self, matrix, r, c):
        return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])

    def solve(self, matrix, r, c, target):
        seen = set()
        original = matrix[r][c]
        stack = [(r, c)]
        while len(stack) > 0:
            r_, c_ = stack.pop()
            matrix[r_][c_] = target
            nbrs = [(r_-1,c_), (r_,c_-1), (r_+1,c_), (r_,c_+1)]
            for r_n, c_n in nbrs:
                if not self.bounds(matrix, r_n, c_n):
                    continue
                if (r_n, c_n) in seen:
                    continue
                if matrix[r_n][c_n] != original:
                    continue
                stack.append((r_n, c_n))
                seen.add((r_n, c_n))
        return matrix