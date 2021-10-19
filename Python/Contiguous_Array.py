class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mx=0
        d={0:-1}
        cnt=0
        l=0
        for i in range(len(nums)):
            if nums[i]==0:
                cnt-=1
            else:
                cnt+=1
            if cnt not in d:
                d[cnt]=i
            else:
                l=i-d[cnt]
            if l>mx:
                mx=l
        return mx
