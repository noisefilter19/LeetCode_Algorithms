"""
Topics: | Math | Binary Search|
"""

class Solution:

    # Iterative method
    def myPow(self, x, n):
        """
        Time:  O(log(n))
        Space: O(1)
        """
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result


#     # Recursive method
#     def myPow(self, x, n):
#         """
#         Time:  O(log(n))
#         Space: O(log(n))
#         """
#         if n < 0:
#             x = 1 / x
#             n = -n

#         if n == 0:
#             return 1
#         elif n == 1:
#             return x

#         half = self.myPow(x, n // 2)
#         if n % 2 == 1:
#             return x * half * half
#         else:
#             return half * half
