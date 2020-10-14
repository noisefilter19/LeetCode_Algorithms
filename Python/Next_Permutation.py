# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while(i >= 0 and nums[i] >= nums[i + 1]):
            i -= 1
        
        if(i == -1):
            nums.sort()
            return
        
        j = len(nums) - 1
        while(j > i):
            if(nums[j] > nums[i]):
                nums[j], nums[i] = nums[i], nums[j]
                break
            j -= 1
        
        start = i + 1
        end = len(nums) -1
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
