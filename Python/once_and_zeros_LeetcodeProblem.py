class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count_dic = self.preProcess(strs)
        return self.dp(m, n, strs, 0, len(strs), {}, count_dic)

    def preProcess(self, strs):
        dic = {}
        for n in range(len(strs)):
            zeroes, ones = 0, 0
            for elt in strs[n]:
                if elt == '0':
                    zeroes += 1
                else:
                    ones += 1
            dic[n] = (zeroes, ones)
        return dic

    def dp(self, m, n, strs, ind, str_len, memo, count_dic):
        if ind == str_len:  # base case, beyond boundary of strs
            return 0
        elif (m, n, ind) in memo:
            return memo[(m, n, ind)]
        elif m == 0 and n == 0:  # base case, "wallet" is empty
            memo[(m, n, ind)] = 0
            return 0
        else:
            c1 = self.dp(m, n, strs, ind+1, str_len, memo,
                         count_dic)  # move on without taking
            zeroes = count_dic[ind][0]
            ones = count_dic[ind][1]
            c2 = 0
            if zeroes <= m and ones <= n:  # check to make sure we can "afford"
                c2 = 1 + self.dp(m-zeroes, n-ones, strs, ind+1,
                                 str_len, memo, count_dic)  # take and move on
            memo[(m, n, ind)] = max(c1, c2)
            return max(c1, c2)
