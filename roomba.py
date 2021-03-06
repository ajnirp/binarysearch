# https://binarysearch.com/problems/Roomba

class Solution:
    def solve(self, moves, x0, y0):
        x, y = 0, 0
        for move in moves:
            if move[0] == 'N':
                y += 1
            elif move[0] == 'E':
                x += 1
            elif move[0] == 'W':
                x -= 1
            elif move[0] == 'S':
                y -= 1
        return x == x0 and y == y0