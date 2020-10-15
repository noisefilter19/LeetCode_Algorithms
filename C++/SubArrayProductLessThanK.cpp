class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if(k<=1) return 0;
        long long product=1;
        int ans,left;
        ans=left=0;
        
       
        for (int right=0; right <nums.size();++right)
           {
            int val=nums[right];
            product *= val;
            while(product >= k)
                {
                product /= nums[left];
                left += 1;
                }
            ans += right - left + 1;
            }
        return ans;
    }
};
