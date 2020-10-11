"""
Topics: | Two Pointers | String |
"""

class Solution:

    def isPalindrome(self, s):
        """
        Time:  O(n)
        Space: O(1)
        """
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
