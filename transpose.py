# https://binarysearch.com/problems/Transpose-of-a-Matrix

class Solution:
    def solve(self, matrix):
        if len(matrix) == 0:
            return matrix
        nr = len(matrix)
        nc = len(matrix[0])
        result = [[None for _ in range(nr)] for _ in range(nc)]
        for r in range(nr):
            for c in range(nc):
                result[c][r] = matrix[r][c]
        return result