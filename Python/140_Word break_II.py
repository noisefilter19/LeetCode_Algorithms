"""
Link : https://leetcode.com/problems/word-break-ii/

140. Word Break II (Hard)

Given a string s and a dictionary of strings wordDict,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Solution:
    
    def __init__(self):
        self.dp = {}
    
    def wordBreak(self, s: str, d: List[str]) -> bool:

        res = []
        if s in d:
            res.append(s)
        
        for i in range(1,len(s)):
            if s[:i] in d:
                t1 = s[:i]
                t2 = s[i:]
                if t2 in self.dp:
                    tt = self.dp[t2]
                else:
                    tt = self.wordBreak(t2, d)
                    self.dp[t2] = tt
                for k in tt:
                    res.append(t1 + " " + k)
        
        return res