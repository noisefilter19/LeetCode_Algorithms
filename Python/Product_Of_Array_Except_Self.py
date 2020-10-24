import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        rght=[]
        lft=[]
        prod=[]
        
        a=1
        for i in range(l):
            rght.append(a)
            a*=nums[i]
        
        a=1
        for i in range(l-1,-1,-1):
            lft.append(a)
            a*=nums[i]
        
        lft=lft[::-1]
        
        for i in range(l):
            prod.append(lft[i]*rght[i])
        
        return prod
