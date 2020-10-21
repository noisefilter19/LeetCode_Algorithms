// https://leetcode.com/problems/next-permutation/
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int g=-1,s=-1,n=nums.size(),i=n-1;
        for(i=n-1;i>0;i--){
            if(nums[i]>nums[i-1]){
                g=s;
                s=i-1;
                break;
            }
        }
        if(s!=-1){
            for(i=n-1;i>g;i--){
                if(nums[i]>nums[s]){
                    g=i;
                    break;
                }
            }
            swap(nums[g],nums[s]);
            reverse(nums.begin()+s+1,nums.end());
        }
        else
            reverse(nums.begin(),nums.end());
    }
};