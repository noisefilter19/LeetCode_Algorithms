# Leetcode problem link: https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals based on the start of interval
        # in case of same first element, list with greater end element should come first
        # eg [1,5], [1,17] -> [1,17], [1,5]
        intervals.sort(key=lambda x: [x[0], -x[1]])
        answer = len(intervals)
        maxEnd = 0 # keeping track of max end of interval
        for interval in intervals: 
            if interval[1] <= maxEnd:
                answer -= 1
            maxEnd = max(maxEnd, interval[1])
        return answer
