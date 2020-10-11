// Leetcode problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> vec(nums1);
        for(auto i:nums2)
        {
            vec.push_back(i);
        }
        sort(vec.begin(),vec.end());
        int num=vec.size();
        double median=0;
        if(num%2==0)
        {
            median=(double)(vec[(num-1)/2] + vec[((num-1)/2)+1]) / 2;
        }
        if(num%2!=0)
        {
            median=(double)vec[(num-1)/2];
        }
        return median;
        
    }
};
