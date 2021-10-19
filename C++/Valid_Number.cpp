//https://leetcode.com/problems/valid-number
class Solution {
public:
    bool isNumber(string s) {
        int n=s.length();
        if(n==0)
            return false;
        if(n==1&&(s[0]<'0'||s[0]>'9'))
            return false;
        int i=0;
        while(s[i]==' '&&i<n)
            i++;
        if(i==n)
            return false;
        while(s[n-1]==' '&&i>=0)
            n--;
        if(s[i]=='+'||s[i]=='-')
            i++;
        if(i==n)
            return false;
        bool chcke=false;
        bool chckdec=false;
        if(s[i]=='e')
            return false;
        if(s[i]=='.'&&i+1<n&&s[i+1]>='0'&&s[i+1]<='9')
        {
            i++;
            chckdec=true;
        }
        for(i;i<n;i++)
        {
            if(s[i]>='0'&&s[i]<='9')
            {
                if(i+1<n&&s[i+1]=='.')
                {
                    if(chckdec==false)
                        chckdec=true;
                    else
                        return false;
                    i++;
                }
            }
            else if(s[i]=='e')
            {
                if(i+1==n)
                    return false;
                if(chcke==true)
                    return false;
                chcke=true;
                if(s[i+1]=='+'||s[i+1]=='-')
                {
                    i++;
                    if(i+1==n)
                        return false;
                }
                chckdec=true;
            }
            else
                return false;
        }
    return true;   
    }
};