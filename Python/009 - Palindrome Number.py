"""
Topics: | Math |

It's possible to halve the time complexity of this solution by only reversing
half of the number, then checking that against the remaining half of the 
original number. I opted for the slightly clearer code.
"""

class Solution:

    def isPalindrome(self, x):
        """
        Time:  O(log(x))
        Space: O(1)
        """
        if x < 0:
            return False
        else:
            return x == self.reverseInt(x)

    def reverseInt(self, x):
        """Return the reversed version of a positive int."""
        reverse = 0
        while x:
            reverse *= 10
            reverse += x % 10
            x //= 10
        return reverse
