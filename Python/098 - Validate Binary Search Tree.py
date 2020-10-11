"""
Topics: | Tree | Depth-first Search |
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isValidBST(self, root: 'TreeNode') -> 'bool':
        """
        Time:  O(n)
        Space: O(n)
        """
        def helper(root, min_val, max_val):
            if not root: return True
            if min_val < root.val < max_val:
                return (helper(root.left, min_val, root.val)
                    and helper(root.right, root.val, max_val))
            return False

        return helper(root, float('-inf'), float('inf'))
