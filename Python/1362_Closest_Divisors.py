# Problem link: https://leetcode.com/problems/closest-divisors/

# Given an integer num, find the closest two integers in absolute difference
# whose product equals num + 1 or num + 2.
# Return the two integers in any order.

# Example 1:
# Input: num = 8
# Output: [3,3]
# Explanation: For num + 1 = 9, the closest divisors are 3 & 3,
# for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.

# Example 2:
# Input: num = 123
# Output: [5,25]

# Example 3:
# Input: num = 999
# Output: [40,25]

"""
Approach:
1. Get factors for num+1 and num+2.
2. Iterate through them to find the closest pair.
"""


class Solution:
    def factors(self, n):
        return [[i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0]

    def closestDivisors(self, num: int) -> list[int]:
        factors = self.factors(num + 1)
        factors.extend(self.factors(num + 2))
        f1, f2 = factors[0]
        for x, y in factors:
            if abs(x - y) < abs(f1 - f2):
                f1, f2 = x, y
        return [f1, f2]
