# https://binarysearch.com/problems/Wolf-of-Wall-Street

class Solution:
    def solve(self, prices):
        if len(prices) < 2:
            return 0
        min_so_far = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price - min_so_far > max_profit:
                max_profit = price - min_so_far
            min_so_far = min(min_so_far, price)
        return max_profit