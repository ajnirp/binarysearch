# https://binarysearch.com/problems/Merging-Binary-Trees

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, node0, node1):
        if not node0 and not node1:
            return None
        elif node0 and not node1:
            return node0
        elif node1 and not node0:
            return node1
        else:
            left_recur = self.solve(node0.left, node1.left)
            right_recur = self.solve(node0.right, node1.right)
            return Tree(node0.val+node1.val, left_recur, right_recur)

# t0 = Tree(0,
#           Tree(3),
#           Tree(2,
#                Tree(3)))

# t1 = Tree(7,
#           Tree(5),
#           Tree(1))

# t = Solution().solve(t0, t1)

# def preorder(t):
#     def helper(u):
#         if not u:
#             return
#         helper(u.left)
#         print(u.val, sep=' ')
#         helper(u.right)
#     helper(t)
#     print()

# preorder(t)
