# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return list()
        levels=[]
        q=[(0,root)]
        res=[]
        while q:
            cur=q[0]
            if cur[0] not in levels:
                levels.append(cur[0])
                res.append([])
            res[cur[0]].append(cur[1].val)
            del q[0]
            if cur[1].left:
                q.append((cur[0]+1,cur[1].left))
            if cur[1].right:
                q.append((cur[0]+1,cur[1].right))
        
        return res
