# https://binarysearch.com/problems/Rotate-List-Left-by-K

# linear space complexity
class Solution:
    def solve(self, nums, k):
        return nums[k:] + nums[:k]

# in-place
# reverse the entire array, then reverse the first N-k elements, then reverse
# the next k elements.
class Solution:
    def rev(self, nums, start, end):
        if start < 0 or end > len(nums)-1:
            return
        mid = (end-start)//2
        for i in range(mid+1):
            nums[start+i], nums[end-i] = nums[end-i], nums[start+i]

    def solve(self, nums, k):
        self.rev(nums, 0, len(nums)-1)
        self.rev(nums, 0, len(nums)-k-1)
        self.rev(nums, len(nums)-k, len(nums)-1)
        return nums

nums = [1, 2, 3, 4, 5, 6]
k = 2
print(Solution().solve(nums, k))