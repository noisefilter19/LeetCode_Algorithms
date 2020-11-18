# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        li = [-1, -1]
        low = 0
        high = len(nums) - 1
        target1 = float('inf')
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                target1 = mid
               
                break
        if target1 == float('inf'):
            return li
        first = self.first(nums, low, target1 - 1, target1)
        second = self.last(nums, target1 + 1, high, target1)
        ls = []
        ls.append(first)
        ls.append(second)
        return(ls)
       
       
    def first(self, nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < nums[target]:
                low = mid + 1
            elif nums[mid] > nums[target]:
                high = mid - 1
            else:
                target = mid
                high = mid - 1
        return target
   
    def last(self, nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[target]:
                high = mid - 1
            elif nums[mid] < nums[target]:
                low = mid + 1
            else:
                target = mid
                low = mid + 1
        return target
