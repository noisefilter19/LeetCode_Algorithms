/*
https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.
You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.
*/
class Solution {
public:
    unordered_map<int, int> dp;
    
    int fun(int n){
        if(dp.count(n))return dp[n];
        int res=INT_MAX;
        if(n%2==0 && n%3==0){
            res = min(res, 1+fun(n/2));
            res = min(res, 1+fun(n/3));
        }
        else if(n%3==0){
            res = min(res, 1+fun(n/3));
            res = min(res, 1+fun(n-1));
        }
        else if(n%2==0){
            res = min(res, 1+fun(n/2));
            res = min(res, n%3 + fun(n-n%3));
        }
        else{
            res = min(res, 1+fun(n-1));
            res = min(res, n%3 + fun(n-n%3));
        }
        return dp[n]=res;
    }
    
    int minDays(int n) {      
        dp[0]=0;
        dp[1]=1;
        return fun(n);
    }
};
