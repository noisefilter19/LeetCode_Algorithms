# https://leetcode.com/contest/biweekly-contest-37/submissions/detail/409863464/
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr = sorted(arr)
        starti = int(n * 0.05)
        new_arr = arr[starti:n-starti]
        new_len = len(new_arr)
        if new_len == 0:
            return 0
        ans = sum(new_arr)/new_len
        return ans
