"""
Topics: | String | Two Pointers |
"""

class Solution:

    def strStr(self, haystack, needle):
        """
        Time:  O(h(h-n))  [where h = len(haystack), n = len(needle)]
        Space: O(1)

        This is just naive pattern matching. Bettter algorithms exist,
        with linear runtimes (e.g., O(h + n)).
        """
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
