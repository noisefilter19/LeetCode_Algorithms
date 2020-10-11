"""
Topics: | Array | Dynamic Programming |
"""

class Solution:

    def maxProfit(self, prices):
        """
        Time:  O(n)
        Space: O(1)
        """
        min_seen = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_seen:
                min_seen = price
            else:
                max_profit = max(max_profit, price - min_seen)
        return max_profit
