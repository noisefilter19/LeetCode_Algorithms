class Solution:
    def wordBreak(self, s, wordDict):
        dic = {}
        for word in wordDict:
            if len(word) in dic:
                dic[len(word)].append(word)
            else:
                dic[len(word)] = [word]
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            for j in dic:
                if i - j + 1 >= 0 and dp[i - j + 1] and s[i - j + 1 : i + 1] in dic[j]:
                    dp[i + 1] = True
        return dp[-1]
