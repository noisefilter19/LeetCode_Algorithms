//https://leetcode.com/problems/merge-intervals/  (Medium)
bool comp(vector<int>a, vector<int>b)
{
    if (a[0] != b[0])
        return a[0] < b[0];
    return a[1] > b[1];
}
class Solution {
public:

    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), comp);
        vector<int>v; vector<vector<int>>ans;
        int s = -1, e = -1;
        for (int i = 0; i < intervals.size(); i++)
        {
            if (s == -1)
            {
                s = intervals[i][0];
                e = intervals[i][1];
            }
            else
            {
                int ss = intervals[i][0];
                int ee = intervals[i][1];
                if (ss >= s and ss <= e)
                {
                    e = max(e, ee);
                }
                else
                {
                    v.push_back(s);
                    v.push_back(e);
                    ans.push_back(v);
                    v.clear();
                    s = ss, e = ee;
                }
            }
        }
        v.push_back(s);
        v.push_back(e);
        ans.push_back(v);
        v.clear();
        //s=ss,e=ee;
        return ans;
    }
};