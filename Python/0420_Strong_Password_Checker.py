class Solution():
    def strongPasswordChecker(self, s: str) -> int:
        
        #Alphabet reach check
        count = 3
        if any('a' <= c <= 'z' for c in s): 
            count -= 1
        if any('A' <= c <= 'Z' for c in s): 
            count -= 1
        if any(c.isdigit() for c in s): 
            count-= 1
        
        #length check
        change = 0
        a = 0
        b = 0
        #consecutive 3 letters check
        c = 2
        while c < len(s):
            if s[c] == s[c-1] == s[c-2]:
                length = 2
                while c < len(s) and s[c] == s[c-1]:
                    length += 1
                    c += 1
                    
                change += length // 3
                if length % 3 == 0: a += 1
                elif length % 3 == 1: b += 1
            else:
                c += 1
       
       
        if len(s) < 6:
            return max(count, 6 - len(s))
        elif len(s) <= 20:
            return max(count, change)
        else:
            delete = len(s) - 20
            change -= min(delete, a)
            change -= min(max(delete - a, 0), b * 2) // 2
            change -= max(delete - a - 2 * b, 0) // 3
                
            return delete + max(count, change)

obj = Solution()
password = ""
output = obj.strongPasswordChecker(password)
print(output)
