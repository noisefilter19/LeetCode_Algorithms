# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Difficuly: Medium
# Runtime : O(N)
# Space: O(1)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(0, len(nums)): 
            if nums[abs(nums[i])-1] >= 0: 
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1] 
            else:
                res.append(abs(nums[i]))
        return res