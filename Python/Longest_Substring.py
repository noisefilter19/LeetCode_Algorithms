class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt={}
        cnt=0
        mx=0
        i=0
        while i<len(s):
            if s[i] not in lt:
                cnt+=1
                lt[s[i]]=i
                i+=1
            else:
                if cnt>mx:
                    mx=cnt
                i=lt[s[i]]+1
                lt={}
                cnt=0
        if cnt>mx:
            mx=cnt
        return mx
