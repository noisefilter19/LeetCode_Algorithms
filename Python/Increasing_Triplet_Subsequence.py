class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        counter = 1
        stack = []
        for i in nums:
            if len(stack) == 0:
                stack.append(i)
            elif i < stack[0]:
                stack[0] = i
            elif len(stack) == 1 and i > stack[0]:
                stack.append(i)
            elif len(stack) == 2 and stack[0] < i < stack[1]:
                stack[1] = i
            elif len(stack) == 2 and i > stack[1]:
                return True
        return False