class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        l=len(num)
        a=[]
        for i in range(l):
            while k>0 and len(a)>0 and int(a[-1])>int(num[i]):
                a.pop()
                k-=1
            a.append(num[i])
        while k>0:
            a.pop()
            k-=1
        if len(a)==0:
            return "0"
        else:
            return str(int("".join(a)))
        
