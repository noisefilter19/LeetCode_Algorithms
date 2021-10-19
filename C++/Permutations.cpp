class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> temp;
        backtrack(res,temp,nums,nums.size());
        return res;
    }
    void backtrack(vector<vector<int>>& res,vector<int> temp,vector<int> nums, int n){
        if(n==0){
            res.push_back(temp);
            return;
        }
        for(int i=0;i<n;i++){
            temp.push_back(nums[i]);
            vector<int> temporaryNums = nums;
            temporaryNums.erase(temporaryNums.begin()+i);
            backtrack(res,temp,temporaryNums,n-1);
            temp.pop_back();
        }
    }
};
