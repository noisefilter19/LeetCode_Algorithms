"""
Topics: | Binary Search Tree |
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def rangeSumBST(self, root, L, R):
        """
        Time:  O(k + log(n)) average; O(n) worst
        Space: O(log(n)) average; O(n) worst
		
		[k = number of nodes between L and R]
        """
        if not root:
            return 0

        range_sum = 0
        if L <= root.val <= R:
            range_sum += root.val
        if L <= root.val:
            range_sum += self.rangeSumBST(root.left, L, R)
        if R > root.val:
            range_sum += self.rangeSumBST(root.right, L, R)
        return range_sum
