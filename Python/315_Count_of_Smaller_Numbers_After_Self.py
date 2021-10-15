'''
Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

315. Count of Smaller Numbers After Self (Hard)

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        out = []
        sorted = []
        for num in nums:
            c = bisect.bisect_left(sorted, num)
            out.append(c)
            bisect.insort(sorted, num)
        return out[::-1]
