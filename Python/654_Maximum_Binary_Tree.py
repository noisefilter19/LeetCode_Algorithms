# Problem link: https://leetcode.com/problems/maximum-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) > 0:
            max_elem = max(nums)
            max_pos = nums.index(max_elem)
            nums.remove(max_elem)
            return TreeNode(max_elem,
                            self.constructMaximumBinaryTree(nums[:max_pos]),
                            self.constructMaximumBinaryTree(nums[max_pos:]))
        return None