class Solution(object):
    def getCharsForDigit(self, x):
        if x == 2:
            return ['a', 'b', 'c']
        elif x == 3:
            return ['d', 'e', 'f']
        elif x == 4:
            return ['g', 'h', 'i']
        elif x == 5:
            return ['j', 'k', 'l']
        elif x == 6:
            return ['m', 'n', 'o']
        elif x == 7:
            return ['p', 'q', 'r', 's']
        elif x == 8:
            return ['t', 'u', 'v']
        elif x == 9:
            return ['w', 'x', 'y', 'z']
        return []
    
    def addNewDigit(self, digit, myList):
        c=self.getCharsForDigit(digit)
        if len(myList) == 0:
            return c
        ans=[]
        for each in myList:
            for char in c:
                ans.append(each+char)
        return ans
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        print(len(digits))
        if len(digits) < 1:
            return []
        l=[]
        for digit in digits:
            l=self.addNewDigit(ord(digit)-48, l)
        return l
