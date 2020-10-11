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

    def insertIntoBST(self, root, val):
        """
        Time:  O(log(n))  [average case]
        Space: O(1)
        """
        new_node = TreeNode(val)

        if not root:
             return new_node

        curr = root
        while True:
            if curr.val > val:
                if not curr.left:
                    curr.left = new_node
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                    break
                else:
                    curr = curr.right
        return root
