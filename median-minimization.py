# https://binarysearch.com/problems/Median-Minimization

# idea: greedy approach. sort the list and put odd items in one list, even items
# in another. this minimises the difference of medians. no need to form the
# lists, though. it's enough to just find the difference of the two middle
# elements, since we know that they will end up being the medians.
class Solution:
    def solve(self, nums):
        nums.sort()
        mid = len(nums) // 2
        return nums[mid] - nums[mid-1]