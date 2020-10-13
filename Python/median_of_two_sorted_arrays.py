class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1 == [0] * len(nums1) and nums2 == [0] * len(nums2):
            return 0.00000
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 != 0:
            return nums[len(nums) // 2]
        elif len(nums) % 2 == 0:
            twoNS = float(nums[len(nums)/2] + nums[len(nums)/2 - 1])
            print(twoNS / 2)
            return twoNS / 2
