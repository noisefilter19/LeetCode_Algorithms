class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        vector<int> positives;
        for(int i: nums)
        {
            if(i > 0)
                positives.push_back(i);
        }
        for(int i = 1; i < INT_MAX; i++)
        {
            if(!count(positives.begin(), positives.end(), i))
            {
                return i;
            }
            
        }
        return -1;
    }
};
