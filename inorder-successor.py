# https://binarysearch.com/problems/Inorder-Successor

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# linear space complexity
class Solution:
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.array.append(node.val)
        self.inorder(node.right)

    def solve(self, root, t):
        self.array = []
        self.inorder(root)
        i = self.array.index(t)
        return self.array[i+1]

# in-place. key idea: update "prev" ptr, but if only if you descend left.
class Solution:
    def leftmost(self, node):
        while node.left:
            node = node.left
        return node

    def find(self, node, val):
        while True:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            else:
                node = node.right

    def solve(self, root, t):
        node = self.find(root, t)
        if node.right:
            return self.leftmost(node.right).val
        ans = None
        while root:
            if root.val > node.val:
                ans = root
                root = root.left
            elif root.val < node.val:
                root = root.right
            else:
                break
        return ans.val
