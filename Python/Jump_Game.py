class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastpos=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=lastpos:
                lastpos=i
        if lastpos==0:
            return True
        else:
            return False
