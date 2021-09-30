# https://leetcode.com/problems/subarray-sum-equals-k/submissions/
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input:nums = [1,1,1], k = 2
# Output: 2
 

# Constraints:

# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

# Approach:
#     Use additional space as mentioned in hint # 2 to exclude nested loop used in brute force method.

from collections import defaultdict 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Using defaultdict to initialize dictionary with value=0
        last_sum = defaultdict(lambda:0) 
        sum_ = 0 
        count = 0 
        for i in range(len(nums)):   
            sum_ += nums[i]  

            if sum_ == k:   
                count += 1  
                
            # Using additional space (last_sum array) to prevent nested loop.
            if sum_ - k in last_sum: 
                count += last_sum[sum_ - k] 
            last_sum[sum_] += 1 
        return count
