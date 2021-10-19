# https://leetcode.com/problems/single-element-in-a-sorted-array/

# Algorithm - Binary Search  

# apply binary search
# if mid is a non extreme element (mid!=0 and mid!=len(arr)) => arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1] =>return arr[mid]
# if mid==0, if arr[mid] != arr[mid +1] => return arr[mid]
# if mid==n-1, if arr[mid] != arr[mid-1] => return arr[mid]
# if mid is even, move to the side of the element same as mid
# if mid is odd, move to side of the element different from mid

class Solution:
    def singleNonDuplicate(self, nums) -> int:

        # n represents the size of the array
        n = len(nums)
        
        # if the size of the array is 1, the only element available is our answer
        if n == 1:
            return nums[0]
        
        # initially start is the first index of the array
        start = 0

        # initially end is the last index of the array
        end = n - 1

        while start <= end:
            mid = start + (end-start)//2

            # if mid is the start index and if element at mid is different from element at mid+1
            # then element at mid is our answer
            if mid == 0 and nums[mid]!=nums[mid+1]:
                return nums[mid]

            # if mid is the last index of the array and if element at mid is different from element at mid-1
            # then element at mid is our answer
            if mid == n - 1 and nums[mid] != nums[mid-1]:
                return nums[mid]

            # if mid is an index somewhere in the middle of the array
            # if element at mid is different from elements at mid-1 and mid+1
            # then mid is our answer
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]

            # now we have cases to move the start and end pointers

            # if mid is even - even number of elements to the left of mid
            if mid%2 == 0:
                # if element at mid is equal to element at mid+1
                # ans will lie to the right of mid
                # start = mid + 1
                # else end = mid - 1
                if nums[mid] == nums[mid+1]:
                    start = mid + 1
                else:
                    end = mid - 1
            
            # if mid is odd - odd number of elements to the left of mid
            else:
                # if element at mid is not equal to element at mid-1
                # then our ans lies to the right side of mid
                # so start = mid + 1
                # else end = mid - 1
                if nums[mid] != nums[mid + 1]:
                    start = mid + 1
                else:
                    end = mid - 1