class Solution:
    
    def helper(self, root):
        if not root:
            return 0
        
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        self.ans = max(self.ans, left + right + root.val)
        return max(left, right) + root.val
    
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        self.helper(root)
        return self.ans
