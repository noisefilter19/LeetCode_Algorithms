# Leetcode problem link: https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numsDict = {}
        answer = 0
        for i in nums:
            if i not in numsDict:
                numsDict[i] = 1
            else:
                numsDict[i]+=1
        for key in numsDict.keys():
            if key+k not in numsDict:
                continue
            # there should be atleast 1 instance of key
            if k != 0 and numsDict[key+k] >= 1:
                answer += 1
            # else if k == 0, that element needs to be present atleast 2 times
            elif numsDict[key+k] >= 2:
                answer += 1
                
        return answer
