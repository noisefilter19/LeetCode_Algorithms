# Problem link: https://leetcode.com/problems/one-edit-distance/

# Given two strings s0 and s1 determine whether they are
# one or zero edit distance away.
# An edit can be described as deleting a character, adding a character,
# or replacing a character with another character.
# Constraints
# 	n ≤ 100,000 where n is the length of s0.
# 	m ≤ 100,000 where m is the length of s1.

# Example 1
# Input
# 	s0 = "mergesort"
# 	s1 = "mergesorts"
# Output
# 	True
# Explanation
# 	This has the edit distance 1, since s was added to the second string.

# Example 2
# Input
# 	s0 = "mergeport"
# 	s1 = "mergesorts"
# Output
# 	False
# Explanation
# 	This has edit distance of 2.

"""
Approach:
1. If length difference:
    is > 1:
        They can't be one edit distance away.
    is == 1:
        There could be an extra element in the longer string.
        So iterate through both and if a char does not match, skip once.
        If another character does not match, then the strings are not
        one edit distance away.
        If the strings are same and longer one has one extra character
        at the end, return True.
    is == 0:
        The strings can differ at most one character.
        So False if more than once.
"""


class Solution:
    def solve(self, s0, s1):
        if len(s0) < len(s1):
            s0, s1 = s1, s0
        count = len(s0) - len(s1)
        if count > 1:
            return False
        elif count == 1:
            i, j, skip = 0, 0, True
            while i < len(s0) and j < len(s1):
                if s0[i] != s1[j]:
                    if skip:
                        j -= 1
                        skip = False
                    else:
                        return False
                i += 1
                j += 1
            return True
        else:
            return [x == y for x, y in zip(s0, s1)].count(False) <= 1
