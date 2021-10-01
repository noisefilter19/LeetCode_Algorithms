'''Question : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.'''

#Solution :

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return float('inf')
        low = 0
        high = len(nums) - 1
        while low <= high:
            if low == high:
                return nums[low]
            mid = low + (high - low) // 2
            ele = nums[mid]
            if ele > nums[high]:
                low = mid + 1
            elif ele == nums[high]:
                if ele != nums[low]:
                    if nums[mid - 1] > ele:
                        return ele
                    high = mid - 1
                else:
                    return min(self.findMin(nums[ : mid]), self.findMin(nums[mid + 1 : ]))
            else:
                if mid == 0 or nums[mid - 1] > ele:
                    return ele
                high = mid - 1