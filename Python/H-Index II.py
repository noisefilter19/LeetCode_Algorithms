class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n
        # We use binary search for faster searching with O(log n) Time
        while left < right:
            mid = left + (right - left) // 2
            if citations[n - 1 - mid] < mid + 1:
                right = mid
            else:
                left = mid + 1
        return left
