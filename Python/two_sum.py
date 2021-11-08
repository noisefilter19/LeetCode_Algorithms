class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values = {}
        
        for index, value in enumerate(nums):
            if target - value in seen_values:
                return seen_values[target - value], index
            
            else:
                seen_values[value] = index
                
        return -1
