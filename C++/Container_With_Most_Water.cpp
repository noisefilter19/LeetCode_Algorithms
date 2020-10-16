/*
Problem Link: https://leetcode.com/problems/container-with-most-water/
Author: Shrey Rai
*/
class Solution {
public:
    int maxArea(vector<int>& height) {
        int n=height.size();
        int i=0,j=n-1;
        int f=0;
        while(i<j)
        {
            int h = min(height[i],height[j]);
            f=max(f,(j-i)*h);
            while(height[i]<=h && i<j)
                i++;
            while(height[j]<=h && j>i)
                j--;
        }

        return f;

    }
};
