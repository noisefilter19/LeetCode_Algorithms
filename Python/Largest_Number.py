# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        new_array = self.merge(nums, 0, len(nums))
        i = 0
        while i < len(new_array) and new_array[i] == '0':
            i += 1
        return '0' if i == len(new_array) else "".join(new_array[i:])
    
    def merge_arrays(self, parted_arr1, parted_arr2):
        i = j = 0
        merged_array = []
        while i < len(parted_arr1) and j < len(parted_arr2):
            if int(parted_arr1[i] + parted_arr2[j]) >= int(parted_arr2[j] + parted_arr1[i]):
                merged_array.append(parted_arr1[i])
                i += 1
            else:
                merged_array.append(parted_arr2[j])
                j += 1
        while i < len(parted_arr1):
            merged_array.append(parted_arr1[i])
            i += 1
        while j < len(parted_arr2):
            merged_array.append(parted_arr2[j])
            j += 1
        return merged_array

    def merge(self, nums, low, high):
        if high - low <= 1:
            return [nums[low]]
        mid = (low + high)//2
        parted_subarray1 = self.merge(nums, low, mid)
        parted_subarray2 = self.merge(nums, mid, high)
        return self.merge_arrays(parted_subarray1, parted_subarray2)
