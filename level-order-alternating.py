# https://binarysearch.com/problems/Level-Order-Alternating

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        curr_level = [root]
        left_to_right = True
        result = []
        while True:
            if left_to_right:
                for node in curr_level:
                    result.append(node.val)
            else:
                for node in reversed(curr_level):
                    result.append(node.val)
            next_level = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if len(next_level) > 0:
                curr_level = next_level
                left_to_right = not left_to_right
            else:
                break
        return result