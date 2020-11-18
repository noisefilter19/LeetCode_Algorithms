#Objective: if a root node of a BST is given, then we have to return the sum of the values of all the nodes between L and R(inclusive).
#This question is asked by many companies. You can code it in your own language, but I found Python implementation to be fairly easy.
#bascially we traverse through all the nodes and if they are in the specified range, we add them to the running sum and finally return the result.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        if root == None :
            return sum
        r = [root]
        while r:
            node = r.pop()
            if node:
                if L<=node.val <= R:
                    sum+= node.val
                if L<node.val:
                    r.append(node.left)
                if node.val < R:
                    r.append(node.right)
        return sum
  # It is requested not to copy the solution as such and use it on LeetCode. It's fairly easy and can be looked up here as reference.
