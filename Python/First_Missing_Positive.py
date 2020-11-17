class Solution(object):
    def firstMissingPositive(self, nums):
        nums = [x for x in nums if x >= 1]
        smallest = 1
        while True:
            if smallest not in nums:
                return smallest
            smallest += 1
