//https://leetcode.com/problems/counting-bits/
/*
Runtime: 4 ms
Memory Usage: 8 MB
*/
class Solution {
public:
    vector<int> countBits(int num) {
    int hold;
    vector <int> ans(num+1);
    for(int i=0;i<=num;i++)
    {
        hold=i/2;
        if(i==0)
            ans[0]=0;
        if(i%2==0)
            ans[i]=ans[hold];
        else
            ans[i]=ans[hold]+1;
    }
    return ans;
    } 
};
