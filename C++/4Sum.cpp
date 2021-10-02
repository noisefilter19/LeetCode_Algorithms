// https://leetcode.com/problems/4sum/
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int i=0;
        vector<vector<int>> res;
        while(i<nums.size()){
            int a1=nums[i];
            int j=i+1;
            while(j<nums.size()){
                int a2=nums[j];
                int tgt=target-a1-a2;
                int front=j+1;
                int back=nums.size()-1;
                while(front<back){
                    int sm=nums[front]+nums[back];
                    if(sm>tgt){
                        back--;
                    }else if(sm<tgt){
                        front++;
                    }else{
                        int f=nums[front];
                        int b=nums[back];
                        res.push_back({a1,a2,f,b});
                        while(front<back && nums[front]==f)
                            front++;
                        while(front<back && nums[back]==b)
                            back--;
                    }
                }
                while(j+1<nums.size()&&nums[j]==nums[j+1])
                    j++;
                j++;
            }
            while(i+1<nums.size()&&nums[i]==nums[i+1])
                i++;
            i++;
        }
        return res;
    }
};
