# Leetcode problem link: https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/

# Problem:
# Given the following definition of binary tree node,
# provide a way to insert a value into the tree.
# It is guaranteed that the value is NOT in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution:
# A naive solution is a recursive one as follows:
#   def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#       if root==None:
#           return TreeNode(val)
#       elif val < root.val:
#           root.left = insertIntoBST(root.left,val)
#           return root
#       else:
#           root.right = insertIntoBST(root.right,val)
#           return root
# The following one is a non-recursive solution

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root==None:
            return TreeNode(val)
        curr = root
        done = False
        while not done:
            if val < curr.val:
                if curr.left==None:
                    curr.left = TreeNode(val)
                    done = True
                else:
                    curr = curr.left
            else:
                if curr.right==None:
                    curr.right = TreeNode(val)
                    done = True
                else:
                    curr = curr.right
        return root

# Note that the problem only checks that the new tree:
# - is a binary tree
# - has the same values from before and the new value
# which means that the binary tree can be rotated
# or altered in other manners.
# This won't affect the answer here, but is important
# when additional structure is added to the tree.