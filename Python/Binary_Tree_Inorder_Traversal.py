#LeetCode problem link: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.node_list = []
        if root != None:
            self.inorder(root)
        return self.node_list
    
    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        self.node_list.append(node.val)
        if node.right:
            self.inorder(node.right)
