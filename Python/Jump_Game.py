# A class with name 'Solution'
class Solution:
    def canJump(self, nums: List[int]) -> bool:         # function in a class
        lastpos=len(nums)-1
        for i in range(len(nums)-1,-1,-1):              # for loop
            if i+nums[i]>=lastpos:                      # if Statement
                lastpos=i
        if lastpos==0:
            return True                                 # return statement
        else:                                           # else statement
            return False
# End of the code
