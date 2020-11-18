#Runtime: better than 87% others

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        The main idea is to iterate over sorted list and instead of looking for a+b+c=0, we look for
        -A = B + C
        In code written as:   -nums[i] = nums[B] + nums[c]
        1) First, we sort list of numbers.
        2) If A is positive, there is no point of checking sums of B+C, since A <= b <= C.
        3) Also, if the number appears twice in input, it appears only once in the solution
        e.g. [-1, -1, -1, -1, 0, 1] => [-1, 0, 1], so we check for that.
        4) Then, we create two pointers in array, starting from highest(C) and lowest(B) value.
        If those numbers add up to the target value, we add solution and start looking for next pair. 
        We make sure we don't add the same solution twice
        If numbers add up to smaller value than target, we have to increase the sum, by taking higher B
        Otherwise (if numbers add up to higher value than target), we decrease sum, by lowering C.
        5) Repeat until B = C
        6) Repeat steps 2-5 for every possible negative target
        """
        nums.sort()
        N = len(nums)
        result = []
        for i in range(N):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            b = i+1
            c = N-1
            while b < c:
                if nums[b] + nums[c] == target:
                    solution = [nums[i], nums[b], nums[c]]
                    result.append([nums[i], nums[b], nums[c]])
                    b = b + 1
                    while b < c and nums[b] == nums[b-1]:
                        b = b + 1
                elif nums[b] + nums[c] < target:
                    b += 1
                else:
                    c -= 1
        return result