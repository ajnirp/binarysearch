# https://binarysearch.com/problems/Conway's-Game-of-Life

''' 
Any living cell with two or three living neighbors lives.
Any dead cell with three living neighbors becomes a live cell.
All other cells die.
'''

class Solution:
    def num_live_nbrs(self, matrix, r, c):
        rows, cols = len(matrix), len(matrix[0])
        delta = [-1, 0, 1]
        nbrs = [(r+dr, c+dc) for dr in delta for dc in delta if not (dr == 0 and dc == 0) and 0 <= r+dr < rows and 0 <= c+dc < cols]
        return sum(matrix[r_][c_] == 1 for r_, c_ in nbrs)

    def solve(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                live_nbrs = self.num_live_nbrs(matrix, row, col)
                if matrix[row][col] == 1 and live_nbrs in [2, 3]:
                    new_matrix[row][col] = 1
                elif matrix[row][col] == 0 and live_nbrs == 3:
                    new_matrix[row][col] = 1
        return new_matrix
