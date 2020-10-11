"""
Topics: | Tree |
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution():

    # Recursive method
    def isUnivalTree(self, root):
        """
        Time:  O(n)
        Space: O(log(n)) average
               O(n) worst
        """
        if not root: return True

        val = root.val

        def dfs(root):
            if not root:
                return True
            if root.val != val:
                return False
            return dfs(root.left) and dfs(root.right)

        return dfs(root)


#     # Iterative method
#     def isUnivalTree(self, root):
#         """
#         Time:  O(n)
#         Space: O(log(n)) average
#                O(n) worst
#         """
#         if not root: return True
#
#         val = root.val
#         stack = []
#         stack.append(root)
#         while stack:
#             node = stack.pop()
#             if node.val != val:
#                 return False
#             if node.right: stack.append(node.right)
#             if node.left:  stack.append(node.left)
#         return True