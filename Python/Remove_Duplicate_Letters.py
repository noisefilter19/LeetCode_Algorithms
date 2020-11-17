class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = []
        lst_occur = {}
        for i in range(len(s)):
            lst_occur[s[i]] = i

        for i in range(len(s)):
            if s[i] in ans:
                continue
            while (ans and (ans[-1] > s[i]) and (lst_occur[ans[-1]] > i)):
                ans.pop()
            ans.append(s[i])
        return ''.join(ans)
