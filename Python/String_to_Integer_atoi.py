# leetcode problem link: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        num, i = [], 0
        while i < len(str) and str[i] == ' ':
            i += 1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            num.append(str[i])
            i += 1
        while i < len(str) and str[i].isdigit():
            num.append(str[i])
            i += 1
        if len(num) == 0:
            return 0
        if not num[-1].isdigit():
            return 0
        ans = int(''.join(num))
        if ans < -(1 << 31):
            return -(1 << 31)
        if ans > (1 << 31) - 1:
            return (1 << 31) - 1
        return ans
