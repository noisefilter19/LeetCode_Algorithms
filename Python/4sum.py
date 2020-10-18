########################
# Author : Abinash Gogoi
########################
class Solution(object):
def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ###########
    #nums.sort()
    ###########
    length = len(nums)
    d = dict()
    for i in xrange(length):
        for j in xrange(i+1, length):
            val = nums[i] + nums[j]
            if val in d:
                d[val].append((i,j))
            else:
                d[val] = [(i,j)]
    res = set()
    for k in d:
        val = target - k
        if val in d:
            firstlist = d[val]
            secondlist = d[k]
            for (i,j) in firstlist:
                for (l,m) in secondlist:
                    thirdlist = [i,j,l,m]
                    if len(set(thirdlist)) != len(thirdlist):
                        continue
                    myList = [nums[i], nums[j], nums[l], nums[m]]
                    myList.sort()
                    res.add( tuple(myList) )
    return list(res)