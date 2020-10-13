//LeetCode Problem link - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution {
public:
    vector<char> getCharsForDigit(int x)
    {
        vector<char> dummy;
        if(x==2)
        {
            vector<char> c;
            c.push_back('a');
            c.push_back('b');
            c.push_back('c');
            return c;
        }
        else if(x==3)
        {
            vector<char> c;
            c.push_back('d');
            c.push_back('e');
            c.push_back('f');
            return c;
        }
        else if(x==4)
        {
            vector<char> c;
            c.push_back('g');
            c.push_back('h');
            c.push_back('i');
            return c;
        }else if(x==5)
        {
            vector<char> c;
            c.push_back('j');
            c.push_back('k');
            c.push_back('l');
            return c;
        }else if(x==6)
        {
            vector<char> c;
            c.push_back('m');
            c.push_back('n');
            c.push_back('o');
            return c;
        }else if(x==7)
        {
            vector<char> c;
            c.push_back('p');
            c.push_back('q');
            c.push_back('r');
            c.push_back('s');
            return c;
        }else if(x==8)
        {
            vector<char> c;
            c.push_back('t');
            c.push_back('u');
            c.push_back('v');
            return c;
        }else if(x==9)
        {
            vector<char> c;
            c.push_back('w');
            c.push_back('x');
            c.push_back('y');
            c.push_back('z');
            return c;
        }
        return dummy;
    }
    
    vector<string> addDigit(int digit,vector<string> v)
    {
        vector<char> c=getCharsForDigit(digit);
        vector<string> ans;
        for(int i=0;i<v.size();i++)
        {
            for(int j=0;j<c.size();j++)
            {
                string temp=v[i];
                temp.push_back(c[j]);
                ans.push_back(temp);
            }
        }
        return ans; 
    }
    vector<string> letterCombinations(string digits) {
        vector<string> v;
        if(digits.size()<1)
            return v;
        v.push_back("");
        for(int i=0;i<digits.size();i++)
        {
            int digit=digits[i]-48;
            //cout<<digit<<endl;
            v=addDigit(digit, v);
        }
        return v;
    }
};
