"""
Topics: | Hash Table |
"""

"""
Unlike the LeetCode solution, this code won't map duplicate
elements in A to the same index in B. This is more consistent
with the usual definition of anagram.
"""

from collections import defaultdict

class Solution:

    def anagramMappings(self, A, B):
        """
        Time:  O(n)
        Space: O(n)
        """
        # Build a dict of lists mapping elements in B
        # to the indices where they occur
        map_B = defaultdict(list)
        for i, elem in enumerate(B):
            map_B[elem].append(i)

        # Lookup an index in B for each element in A
        A_to_B = []
        for elem in A:
            if not map_B[elem]: return []
            B_index = map_B[elem].pop()
            A_to_B.append(B_index)

        return A_to_B
