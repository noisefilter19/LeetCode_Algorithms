# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# 123. Best Time to Buy and Sell Stock III(Hard) Solution
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)

        # helper function that finds maxrise and the lowcations of maxrise in prices[b:e:step]
        def helper(b, e, step):
            max_rise, tmp_low, low, hi = 0, b, 0, 0
            for i in range(b, e, step):
                rise = prices[i] - prices[tmp_low]
                if rise <= 0:
                    tmp_low = i
                elif rise > max_rise:
                    max_rise, low, hi = rise, tmp_low, i
            return max_rise, low, hi

        # For the first pass, we identify the indices for "at most 1 transaction" problem, so that we find low, hi
        max_rise, low, hi = helper(0, l, 1)
        # Then there are three possibilities: 1, use (low, hi) and another rise before low; 2, (low, hi) and another rise after hi; 3, use (low, x) and (y, hi).
        # In the third case, it is equivalent to finding the max_rise in the sequence prices[hi:low:-1]
        m1, m2, m3 = helper(0, low, 1)[0], helper(
            hi+1, l, 1)[0], helper(hi-1, low, -1)[0]
        return max_rise + max(m1, m2, m3)

# Driver code
# test = [3, 3, 5, 0, 0, 3, 1, 4]
# p = Solution()
# result = p.maxProfit(test)
# print(result)
