# 814. Binary Tree Pruning

# Problem link - https://leetcode.com/problems/binary-tree-pruning/

# Algorithm 

# We have two functions
# 1) A helper function to iterate through all nodes
# 2) The actual function that does the checking - check_sub(root)
# Check_Sub checks the subtree of a root and returns False if there is a "1" anywhere under the tree otherwise it implies that subtree contains only zeros and can be deleted according to the given question. 
# You call check_sub whenever you reach a node with value = 0


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root.val ==0 and check_sub(root):
            return None
        temp = root
        helper(root)
        return temp
        
        
def helper(root):
    if root:
        left,right = root.left,root.right
        if left:
            if left.val==0 and check_sub(left):
                root.left=None
            else:
                helper(left)
        if right:
            if right.val==0 and check_sub(right):
                root.right=None
            else:
                helper(right)
def check_sub(root):
    if not root:
        return True
    if root.val==1:
        return False
    return check_sub(root.left) and check_sub(root.right)