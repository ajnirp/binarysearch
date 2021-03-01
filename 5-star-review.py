# https://binarysearch.com/problems/5-Star-Review-Percentage

from math import ceil

class Solution:
    def solve(self, reviews, ratio):
        if ratio in [0, 100]:
            return 0
        ratio /= 100
        f_sum, t_sum = 0, 0
        for f, t in reviews:
            f_sum += f
            t_sum += t
        result = (ratio*t_sum - f_sum) / (1 - ratio)
        # dealing with floating-point error - see if we can get by by rounding
        # down, else round up
        round_down = int(result)
        if (f_sum + round_down) / (t_sum + round_down) >= ratio:
            return round_down
        else:
            return ceil(result)