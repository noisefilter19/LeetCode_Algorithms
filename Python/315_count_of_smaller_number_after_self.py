from bisect import bisect_left


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result, nums_sorted = [0] * len(nums), sorted(nums)
        for i, n in enumerate(nums):
            result[i] = bisect_left(nums_sorted, n)
            nums_sorted.pop(result[i])

        return result
