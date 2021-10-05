#https://leetcode.com/problems/shuffle-an-array/
class Solution:
    def __init__(self, nums):
        self.arr = nums
        self.original = list(nums)

    def reset(self):
        self.arr = self.original
        self.original = list(self.original)
        return self.arr

    def shuffle(self):
        aux = list(self.arr)

        for idx in range(len(self.arr)):
            remove_idx = random.randrange(len(aux))
            self.arr[idx] = aux.pop(remove_idx)

        return self.arr
