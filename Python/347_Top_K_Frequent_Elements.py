class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        t = list(freq.most_common(k))
        return [x[0] for x in t]

