"""
Topics: | Hash Table | Two Pointers | String
"""

class Solution:

    def lengthOfLongestSubstring(self, string):
        """
        Time:  O(n)
        Space: O(k)

        [k = length of the longest substring w/o repeating characters]
        """
        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(string) and right < len(string):
            if string[right] not in chars:
                chars.add(string[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(string[left])
                left += 1
        return longest
