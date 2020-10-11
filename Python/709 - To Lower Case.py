"""
Topics: | String |
"""

class Solution:

    def toLowerCase(self, str):
        """
        Time:  O(n)
        Space: O(n)
        """
        lowercase = [Solution.charToLower(ch) for ch in str]
        return ''.join(lowercase)

    @staticmethod
    def charToLower(ch):
        upper_to_lower = ord('a') - ord('A')
        if 'A' <= ch <= 'Z':
            return chr(ord(ch) + upper_to_lower)
        return ch
