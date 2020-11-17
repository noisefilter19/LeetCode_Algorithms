class Solution(object):
    def uniqueOccurrences(self, arr):
        return len(set({item: arr.count(item) for item in set(arr)}.values())) == len(set(arr))
