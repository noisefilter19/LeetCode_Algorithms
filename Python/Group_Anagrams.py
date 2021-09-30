class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp=[]
        lsts=[]
        d={}
        for i in range(len(strs)):
            lsts.append([])
            for j in strs[i]:
                lsts[i].append(j)
            stl=sorted(lsts[i])
            if tuple(stl) in d:
                d[tuple(stl)].append(strs[i])
            else:
                d[tuple(stl)]=[strs[i]]
        lsts=[]
        for k in d.keys():
            lsts.append(d[k])
        return lsts        
        
