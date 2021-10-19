class Solution:
    def intToRoman(self, num: int) -> str:
        dic={4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
        h=1
        
        s1=""
        s2=""
        s3=""
        s4=""
        while(num!=0):
            dig=num%10
            if h==1:
                if dig==9:
                    s1+=dic[9]
                elif dig>=5:
                    s1+="V"
                    for i in range(dig-5):
                        s1+="I"
                elif dig==4:
                    s1+=dic[4]
                else:
                    for i in range(dig):
                        s1+="I"
                h+=1
            
            elif h==2:
                if dig==9:
                    s2+=dic[90]
                elif dig>=5:
                    s2+="L"
                    for i in range(dig-5):
                        s2+="X"
                elif dig==4:
                    s2+=dic[40]
                else:
                    for i in range(dig):
                        s2+="X"
                h+=1
                
            elif h==3:
                if dig==9:
                    s3+=dic[900]
                elif dig>=5:
                    s3+="D"
                    for i in range(dig-5):
                        s3+="C"
                elif dig==4:
                    s3+=dic[400]
                else:
                    for i in range(dig):
                        s3+="C"
                h+=1
            
            else:
                for i in range(dig):
                    s4+="M"
            num=num//10
        return s4+s3+s2+s1
                
                    
        
