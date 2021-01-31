# https://binarysearch.com/problems/Diagonal-Sort

class Solution:
    def sort_diag(self, matrix, i):
        cols, rows = len(matrix[0]), len(matrix)
        arr = [matrix[j][i+j] for j in range(cols) if i+j < cols and j < rows]
        arr.sort()
        for j in range(cols):
            if i+j < cols and j < rows:
                matrix[j][i+j] = arr[j]

    def sort_diag_2(self, matrix, i):
        cols, rows = len(matrix[0]), len(matrix)
        arr = [matrix[i+j][j] for j in range(rows) if i+j < rows and j < cols]
        arr.sort()
        for j in range(rows):
            if i+j < rows and j < cols:
                matrix[i+j][j] = arr[j]

    def solve(self, matrix):
        for i in range(len(matrix[0])):
            self.sort_diag(matrix, i)

        for i in range(1, len(matrix)):
            self.sort_diag_2(matrix, i)

        return matrix
