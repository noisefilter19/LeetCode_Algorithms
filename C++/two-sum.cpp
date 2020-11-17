#include<bits/stdc++.h>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> id;
        for(int i = 0; i < nums.size(); i++) {
            int make = target - nums[i];
            if(id[make]) {
                return {id[make]-1, i};
            }
            id[nums[i]] = i+1;
        }
        return {-1, -1};
    }
};
