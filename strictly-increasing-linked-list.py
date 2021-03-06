# https://binarysearch.com/problems/A-Strictly-Increasing-Linked-List

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        if head is None:
            return True
        last_seen = head.val
        head = head.next
        while head:
            if head.val <= last_seen:
                return False
            last_seen = head.val
            head = head.next
        return True