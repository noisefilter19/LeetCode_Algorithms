"""
Topics: | String |
"""

class Solution:

    def lengthOfLastWord(self, string):
        """
        Time:  O(n)
        Space: O(1)
        """
        # Skip any trailing spaces
        i = len(string) - 1
        while i >= 0 and string[i] == ' ':
            i -= 1

        # Iterate through the last word
        j = i
        while j >= 0 and string[j] != ' ':
            j -= 1

        return i - j

