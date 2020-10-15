class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int n =  nums.size();
        vector<int> res;
        for(int i=0; i<n;i++){
            cout << "in";
            int &x = nums[abs(nums[i])-1];
            if(x < 0){
                res.push_back(abs(nums[i]));
            } 
            
            // mark as already visited
            x = -x;
            
        }
        return res;
    }
};
