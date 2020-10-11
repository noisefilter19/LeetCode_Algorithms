"""
Topics: | Tree |
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def searchBST(self, root, val):
        """
        Time:  O(log(n))
        Space: O(1)
        """
        curr = root
        while curr and curr.val != val:
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
