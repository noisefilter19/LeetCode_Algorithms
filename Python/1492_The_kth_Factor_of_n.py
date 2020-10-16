class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n):
            if n % i == 0:
                factors.append(i)
        factors.append(n)
        len_array = len(factors)
        print(factors)
        if len_array < k:
            return -1
        else:
            return factors[k-1]