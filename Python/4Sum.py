# https://leetcode.com/problems/4sum/
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        a=[]
        nums=sorted(nums)
        i=0
        while i < len(nums):
            j=i+1
            while j<len(nums):
                tgt=target-nums[i]-nums[j]
                fr=j+1
                bk=len(nums)-1
                while fr<bk:
                
                    if nums[fr]+nums[bk]<tgt:
                        fr+=1
                    
                    elif nums[fr]+nums[bk]>tgt:
                        bk-=1
                    else:    
                        tr=[nums[i],nums[j],nums[fr],nums[bk]]
                        if nums[fr]+nums[bk]==tgt:
                            a.append(tr)
                    
                        while fr<bk and nums[fr]==tr[2]:
                            fr+=1
                    
                        while fr<bk and nums[bk]==tr[3]:
                            bk-=1
                        
                while j<len(nums)-1 and nums[j]==nums[j+1]:
                    j+=1
                j+=1
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                    i+=1
            i+=1
        
        return a
        
