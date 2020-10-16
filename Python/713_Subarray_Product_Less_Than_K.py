# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        def fac(n):
            if n<=1:
                return n
            return int(n*(n+1)/2)

        def get(s,nums,k):
            for i in range(s,len(nums)):
                if nums[i]<k:
                    return i
            return None
        if k<=1:
            return 0
        start=get(0,nums,k)
        if start==None:
            return 0
        ans=0
        product=nums[start]
        for i in range(start+1,len(nums)):
            if product*nums[i]<k:
                product*=nums[i]
            else:
                ans+=(i-start)
                product*=nums[i]
                product/=nums[start]
                start+=1
                while product>=k:
                    product/=nums[start]
                    start+=1
                    ans+=(i-start)+1
        else:
            ans+=fac(i+1-start)
        return ans
