/*
  Problem link: https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
  
  Author: __PRAKHAR__ (leetcode id)
*/

class Solution {
public:
    int minCost(string s, vector<int>& cost) {
        int sum = 0;
        for(int i = 0; i < s.size()-1; i++)
            if(s[i] == s[i+1]){                       
                sum += min(cost[i],cost[i+1]);            
                if(cost[i+1] < cost[i]){                  
                    cost[i+1] = cost[i];
                }
            }
        }
        return sum;
    }
};
