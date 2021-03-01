# https://binarysearch.com/problems/Pairwise-Linked-List-Swap

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        if not node:
            return node
        head = node
        a, b = node, node.next
        while b:
            a.val, b.val = b.val, a.val
            a, b = b, b.next
            if not b:
                break
            a, b = b, b.next
        return head