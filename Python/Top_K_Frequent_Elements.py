# leetcode problem link: https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers_counter = dict(Counter(nums))
        sorted_numbers_counter = sorted(
            numbers_counter.items(), key=lambda x: x[1], reverse=True)
        return [counter[0] for counter in sorted_numbers_counter[:k]]
