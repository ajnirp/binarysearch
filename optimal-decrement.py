# https://binarysearch.com/problems/Optimal-Decrement

# greedy approach works. on each step, decrement the largest number. this yields
# the minimum possible max value. since python's heap implementation is a min-heap,
# negate all numbers before storing, increment rather than decrementing, and
# negate again before returning.

import heapq

class Solution:
    def solve(self, nums, k):
        h = []
        for num in nums:
            heapq.heappush(h, -num)
        for _ in range(k):
            largest = h[0]
            heapq.heappop(h)
            heapq.heappush(h, largest+1)
        return -h[0]