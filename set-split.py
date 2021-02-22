# https://binarysearch.com/problems/Set-Split

class Solution:
    def solve(self, nums):
        if len(nums) == 0:
            return True
        sum_all = sum(nums)
        if sum_all & 1 == 1:
            return False
        nums.sort()
        sum_a = 0
        a = []
        for num in nums[:-1]: # you have to leave at least one element in b
            if sum_a < (sum_all // 2):
                a.append(num)
                sum_a += num
            else:
                break
        return a[-1] < nums[len(a)] and sum_a == (sum_all // 2)

nums = [1, 2, 2, 3]

print(Solution().solve(nums))