"""
Topics: | None |
"""

class Solution:
class Solution:

    def fizzBuzz(self, n):
        """
        Time:  O(n)
        Space: O(n)
        """
        result = []
        for k in range(1, n + 1):
            string = ""
            if k % 3 == 0:
                string += "Fizz"
            if k % 5 == 0:
                string += "Buzz"
            result.append(string if string else str(k))
        return result
