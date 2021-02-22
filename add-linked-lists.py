# https://binarysearch.com/problems/Add-Linked-Lists

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self, l0, l1, carry):
        if not l0 and not l1:
            if carry == 1:
                return LLNode(1)
            else:
                return None
        elif l0 and l1:
            sum_ = l0.val + l1.val + carry
            return LLNode(sum_ % 10, self.helper(l0.next, l1.next, sum_ // 10))
        elif l0 and not l1:
            sum_ = l0.val + carry
            return LLNode(sum_ % 10, self.helper(l0.next, None, sum_ // 10))
        elif not l0 and l1:
            sum_ = l1.val + carry
            return LLNode(sum_ % 10, self.helper(None, l1.next, sum_ // 10))

    def solve(self, l0, l1):
        return self.helper(l0, l1, 0)