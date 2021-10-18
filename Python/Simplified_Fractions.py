# Link: https://leetcode.com/problems/simplified-fractions/submissions/

class Solution:
    def simplifiedFractions(self, n: int):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        sol = []
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if gcd(i, j) == 1:
                    if i == 1 and j == 1:
                        continue
                    ans = str(j) + '/' + str(i)
                    sol.append(ans)
        return sol