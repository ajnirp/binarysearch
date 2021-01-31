# https://binarysearch.com/problems/Subtree

# This could probably be trimmed down a little

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def identical(self, node1, node2):
        if node1 is None and node2 is not None:
            return False

        if node2 is None and node1 is not None:
            return False

        if node1 is None and node2 is None:
            return True
        
        if node1.val != node2.val:
            return False

        return self.identical(node1.left, node2.left) and self.identical(node1.right, node2.right)

    def solve(self, root, target):
        if root is None and target is not None:
            return False

        if target is None and root is not None:
            return False

        if self.identical(root, target):
            return True
        
        return self.solve(root.left, target) or self.solve(root.right, target)