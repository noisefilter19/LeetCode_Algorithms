// https://leetcode.com/problems/reducing-dishes/

class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end(), greater<int>());
        int ans = 0, cur=0;
        for(int n:satisfaction)
        {
            cur +=n;
            if(cur >= 0)
            {
                ans += cur;
            }
        }
        return ans;
    }
};