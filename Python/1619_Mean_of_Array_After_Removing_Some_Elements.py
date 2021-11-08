# Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        min_ = int(len(arr)*0.05)
        max_ = int(len(arr)*0.05)
        new = arr[min_:len(arr)-max_]
        sum_=0
        for i in new:
            sum_ += i
        return(sum_/len(new))
        
