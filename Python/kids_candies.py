class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        l=len(candies)
        ans=[]
        for i in range(l):
            if candies[i]+extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans

