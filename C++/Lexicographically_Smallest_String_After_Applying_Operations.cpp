// Problem Link -
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

class Solution {
public:
    string add(string s,int v)
    {
        int n=s.length();
        for(int i=1;i<n;i+=2)
            s[i]=(s[i]-'0'+v)%10+'0';
        return s;
    }
    string rotate(string s,int b)
    {
        int n=s.length();
        return s.substr(n-b)+s.substr(0,n-b);
    }
    string findLexSmallestString(string s, int a, int b) {
        set<string> vis;
        queue<string> qu;
        qu.push(s);
        vis.insert(s);
        while(!qu.empty())
        {
            string s=qu.front(); qu.pop();
            string ns=add(s,a);
            if(!vis.count(ns))
            {
                vis.insert(ns);
                qu.push(ns);
            }
            ns=rotate(s,b);
            if(!vis.count(ns))
            {
                vis.insert(ns);
                qu.push(ns);
            }
        }
        return *(vis.begin());
    }
};
