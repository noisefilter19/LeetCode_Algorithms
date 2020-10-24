# https://leetcode.com/problems/product-of-array-except-self/

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input: [1,2,3,4]
# Output: [24,12,8,6]

# Constraint:

# It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Approach:

# Multiply all values of nums before and after each index storing the products in an additional array.
# Time Complexity: O(N), Space Complexity: O(N) - where N is length of array.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod_arr = [0]*len(nums)
        left_prod = 1
        for i in range(len(nums)):
            prod_arr[i] = left_prod
            left_prod = left_prod * nums[i]
        
        right_prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod_arr[i] = prod_arr[i] * right_prod
            right_prod = right_prod * nums[i]
        
        return prod_arr
