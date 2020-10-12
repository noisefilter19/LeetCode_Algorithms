# Given a list e.g. [A, B, C]
# return a list of all permutations =>
# [
#   [A,B,C]
#   [A,C,B]
#   [B,A,C]
#   [B,C,A]
#   [C,A,B]
#   [C,B,A]
# ]


class Solution:
    def swap(self, indexA: int, indexB: int, nums: List[int]):
        temp = nums[indexA]
        nums[indexA] = nums[indexB]
        nums[indexB] = temp

    def findPermutations(self, nums: List[int], leftIndex: int, rightIndex: int):

        if leftIndex is rightIndex:
            self.result.append(nums.copy())
            return

        for index in range(leftIndex, rightIndex):
            self.swap(leftIndex, index, nums)

            # we have everything before leftIndex +1 locked in place for this permutation
            self.findPermutations(nums, leftIndex + 1, rightIndex)

            # return array to the initial way it was
            self.swap(leftIndex, index, nums)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        self.findPermutations(nums, 0, len(nums))
        return self.result


# Complexity analysis :)
#
# time complexity: O(n! * n)
# explenation: there are a total of n! permutations and it takes the leftIndex n steps to reach the right index for each of them
#
# space complexity: O(n!)
# explenation: we need to store the resulting permutations until we print them
