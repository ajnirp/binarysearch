# https://binarysearch.com/problems/Consecutive-Ones

class Solution:
    def solve(self, nums):
        seen_block = False
        block_over = False
        for idx in range(len(nums)):
            if seen_block:
                if nums[idx] != 1:
                    block_over = True
                    seen_block = False
            else:
                if nums[idx] == 1:
                    if block_over:
                        return False
                    else:
                        seen_block = True
        return True