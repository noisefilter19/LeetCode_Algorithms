# leetcode problem link: https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_of_ele = len(nums)-1
        for i in range(k):
            temp = nums[num_of_ele]
            nums.pop(num_of_ele)
            nums.insert(0,temp)
        return nums
        
