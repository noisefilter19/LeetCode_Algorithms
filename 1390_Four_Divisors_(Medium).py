def sumDivisors(num):
    divSum = 0
    n = 0
    sqrtDiv = math.sqrt(num)
    if (num % sqrtDiv == 0):
        return 0
    sqrtDiv = math.floor(sqrtDiv)
          
    for i in range(1, sqrtDiv + 1):
        if num % i == 0:
            divSum += i + num // i
            n += 2
            if n > 4:
                return 0
    
    if n == 4:
        return divSum
    else:
        return 0



class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divSum = 0
        for num in nums:
            divSum += sumDivisors(num)
        return divSum
