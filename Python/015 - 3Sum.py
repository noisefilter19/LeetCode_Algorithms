"""
Topics: | Array | Two Pointers |
"""

class Solution:

    def threeSum(self, nums):
        """
        Time:  O(n^2)
        Space: O(1)

        Sort the array. Fix the first element of the triplet,
        then slide a `left` and `right` pointer through the
        subarray to the right of the first element, looking
        for a triplet that adds to 0.
        """
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicate triplets
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left +=1
                elif sum > 0:
                    right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    # Skip duplicate triplets
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1; right -= 1
        return result
