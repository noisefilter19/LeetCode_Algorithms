class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0]
        
        for i in range(1, num+1):
            """
            Every i*2 is just one bit off than i
            If i is odd, then add +1 to i*2 (just to make it odd)
            """

            """Now divide i by 2 and 
            access i//2 element and use above Logic
            """
            j = i >> 1 # divide by 2
            
            if i & 1: #odd
                bits.append(bits[j]+1)
            else:
                bits.append(bits[j])
        return bits                
    
