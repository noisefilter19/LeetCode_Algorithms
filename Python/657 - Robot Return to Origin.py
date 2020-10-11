"""
Topics: | String |
"""

from collections import Counter

class Solution:

    def judgeCircle(self, moves):
        """
        Time:  O(m)  [m = len(moves)]
        Space: O(1)
        """
        move_count = Counter(moves)
        net_horizontal = abs(move_count['L'] - move_count['R'])
        net_vertical = abs(move_count['U'] - move_count['D'])
        return net_horizontal == 0 and net_vertical == 0
