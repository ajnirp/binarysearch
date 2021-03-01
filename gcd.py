# https://binarysearch.com/problems/Greatest-Common-Divisor

class Solution:
    def gcd(self, a, b):
        if a == 0:
            return b
        elif b == 0:
            return a
        if a > b:
            return self.gcd(a%b, b)
        else:
            return self.gcd(a, b%a)

    def solve(self, nums):
        if len(nums) == 1:
            return nums[0]
        result = self.gcd(nums[0], nums[1])
        for i in range(2, len(nums)):
            result = self.gcd(result, nums[i])
        return result