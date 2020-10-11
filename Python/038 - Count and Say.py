"""
Topics: | String |
"""

class Solution:

    def countAndSay(self, n):
        """
        Time and space complexity of this solution depend
        on the rate of growth of the sequence, which looks
        at least polynomial (O(n^c)).
        """
        prev = [1]
        for _ in range(1, n):
            curr = []
            i = 0
            while i < len(prev):
                j = i + 1
                while j < len(prev) and prev[j] == prev[i]:
                    j += 1
                curr.append(j - i)
                curr.append(prev[i])
                i = j
            prev = curr
        return ''.join(map(str, prev))
