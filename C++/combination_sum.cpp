//PROBLEM-LINK=https://leetcode.com/problems/combination-sum/
// Runtime: 4ms
// Memory Usage: 10 MB
class Solution
{
public:
    void cSum(vector<int> &candidates, int target, vector<int> &current, int sum, int index, vector<vector<int>> &result)
    {

        if (sum == target)
        {
            vector<int> temp(current.begin(), current.end());
            sort(temp.begin(), temp.end());
            if (count(result.begin(), result.end(), temp) == 0)
                result.push_back(temp);
            return;
        }

        if (sum > target)
        {
            return;
        }

        for (int i = index; i < candidates.size(); i++)
        {
            current.push_back(candidates[i]);
            cSum(candidates, target, current, sum + candidates[i], i, result);
            current.pop_back();
        }

        return;
    }

    vector<vector<int>> combinationSum(vector<int> &candidates, int target)
    {

        vector<vector<int>> result;
        vector<int> current;

        cSum(candidates, target, current, 0, 0, result);

        return result;
    }
};