// https://leetcode.com/problems/permutation-sequence/
class Solution {
public:
    string getPermutation(int n, int k) {
        vector<bool> chck(n+1,false);
        vector<long long> fac={1,1,2,6,24,120,720,5040,40320,362880};
        string ans;
        int len=0;
        while(len!=n)
        {
            int x=(k-1)/fac[n-len-1];
            k-=fac[n-len-1]*x;
            int count=0;
            for(int i=1;i<=n;i++)
            {
                if(chck[i]==false)
                    count++;
                if(count==(x+1))
                {
                    chck[i]=true;
                    ans+=i+48;
                    len++;
                    break;
                }
            }
        }
        return ans;
    }
};