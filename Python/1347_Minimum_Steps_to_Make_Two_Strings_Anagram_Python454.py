# LeetCode Problem : https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        c=0
        if a==b:
            return 0
        else:
            y=list(set(t))
            for p in range(len(y)):
                l=t.count(y[p])-s.count(y[p])
                if l>0:
                    c+=l
        return c
