class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for(int i=0;i<nums.size();i++){
            int target=-nums[i];
            int front=i+1;
            int back=nums.size()-1;
            while(front<back){
                int sum=nums[front]+nums[back];
                if(sum>target){
                    back--;
                }
                else if(sum<target){
                    front++;
                }else{
                    int f=nums[front];
                    int b=nums[back];
                    res.push_back({nums[i],f,b});
                    while(front<back&&nums[front]==f)
                        front++;
                    while(front<back&&nums[back]==b)
                        back--;
                }
            }
            while(i+1<nums.size() && nums[i+1]==nums[i])
                i++;
        }
        return res;
    }
};
