"""
Topics: | Stack | Tree |
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Iterative method
    def preorderTraversal(self, root):
        """
        Time:  O(n)
        Space: O(log(n)) average
               O(n) worst
        """
        traversal = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                traversal.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        return traversal

#     # Recursive method
#     def preorderTraversal(self, root):
#         """
#         Time:  O(n)
#         Space: O(log(n)) average
#                O(n) worst
#         """
#
#         traversal = []
#
#         def helper(node):
#             if node:
#                 traversal.append(node.val)
#                 helper(node.left)
#                 helper(node.right)
#
#         helper(root)
#         return traversal
