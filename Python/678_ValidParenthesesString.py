class Solution:
    def checkValidString(self, s: str) -> bool:
        low_bound = 0
        high_bound = 0
        
        for char in s: 
            if char == "(":
                low_bound += 1
            else:
                low_bound -= 1
                
            if char != ")":
                high_bound += 1
            else:
                high_bound -= 1
            
            if high_bound < 0:
                break
                
            low_bound = max(low_bound, 0) 
    
    
        return low_bound == 0
        
