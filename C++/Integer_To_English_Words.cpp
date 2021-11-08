//https://leetcode.com/problems/integer-to-english-words
class Solution {
public: vector<string>yo{"","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"};
    
    string help(int num,string add)
    {
        int n=num;
        if(num==0)
            return "";
        string s;
        if(n/100>0)
        {
            s+=yo[n/100];
            s+=" ";
            s+="Hundred ";
        }
        if(num%100<20&&num%100!=0)
        {
            s+=yo[num%100];
            s+=" ";
        }
        else
        {
            switch((n%100)/10)
            {
                case 2: s+="Twenty "; break;
                case 3: s+="Thirty "; break;
                case 4: s+="Forty "; break;
                case 5: s+="Fifty "; break;
                case 6: s+="Sixty "; break;
                case 7: s+="Seventy "; break;
                case 8: s+="Eighty "; break;
                case 9: s+="Ninety "; break;
            }
            if(n%10!=0)
            {
            s+=yo[n%10];
            s+=" ";
            }
        }
        s+=add;
        return s;
    }
    
    string numberToWords(int n) {
        if(n==0)
            return "Zero";
        string s=help(n/1000000000,"Billion ")+help((n%1000000000)/1000000,"Million ")+help((n%1000000)/1000,"Thousand ")+help(n%1000,"");
        int i=s.length()-1;
        while(s[i]<='a'||s[i]>='z')
        {
            s.pop_back();   
            i--;
        }
        return s;
    }
};