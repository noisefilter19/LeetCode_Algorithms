# Problem link:
# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            max_cur = max_prod
            max_prod = max(max_cur * nums[i], min_prod * nums[i], nums[i])
            min_prod = min(max_cur * nums[i], min_prod * nums[i], nums[i])
            res = max(res, max_prod)
        return res
