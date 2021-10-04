'''
Using python's library: collections
# from collections import Counter

Use the counter object to store all frequencies of the list.
Usimg the most_common method, which takes an argument N, signifying the number of most common elements to be returned.

The returned list consists of tuples (num, freq).
Return the first element of each tuple as the final answer.

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        t = list(freq.most_common(k))
        return [x[0] for x in t]

