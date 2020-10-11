// https://leetcode.com/problems/remove-covered-intervals/

class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        
        sort(intervals.begin(), intervals.end(), myFn);
        int end, prev_end = 0;
        int count = 0;
        for(auto curr: intervals) {
            end = curr[1];
            if(prev_end < end){
                ++count;
                prev_end = end;
            }
        }
        return count;
    }
    static bool myFn(vector<int> &a, vector<int> &b){
            return a[0]==b[0] ? a[1]>=b[1]: a[0] < b[0];
    }
};
