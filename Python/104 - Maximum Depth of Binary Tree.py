"""
Topics: | Depth-first Search |
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Iterative solution
    def maxDepth(self, root):
        """
        Time:  O(n)
        Space: O(n) worst; O(log(n)) average
        """
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return max_depth


    # # Recursive solution
    # def maxDepth(self, root):
    #     """
    #     Time:  O(n)
    #     Space: O(n) worst; O(log(n)) average
    #     """
    #     if not root:
    #         return 0
    #     else:
    #         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
