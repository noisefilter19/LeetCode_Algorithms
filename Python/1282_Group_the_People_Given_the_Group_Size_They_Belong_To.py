# Problem link: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i in range(len(groupSizes)):
            try:
                groups[groupSizes[i]].add(i)
            except:
                groups[groupSizes[i]] = {i}
        sol=[]
        for i in groups.keys():
            for _ in range(len(groups[i])//i):
                x = []
                for __ in range(i): 
                    x.append(groups[i].pop())
                sol.append(x)
        return sol
