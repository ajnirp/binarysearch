# https://binarysearch.com/problems/Tree-Traversal

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, moves):
        stack = []
        for move in moves:
            if move == 'UP':
                stack.pop()
            else:
                stack.append(move)
        curr = root
        for move in stack:
            if move == 'LEFT':
                curr = curr.left
            else:
                curr = curr.right
        return curr.val
