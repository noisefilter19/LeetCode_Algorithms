// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> restoreMatrix(vector<int> &rowSum, vector<int> &colSum)
    {
        int m = rowSum.size();
        int n = colSum.size();
        vector<vector<int>> ans(m, vector<int>(n));

        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                ans[i][j] = min(rowSum[i], colSum[j]);
                rowSum[i] -= ans[i][j];
                colSum[j] -= ans[i][j];
            }
        }
        return ans;
    }
};

int main()
{
    Solution a;
    vector<int> rowSum = {5, 7, 10}, colSum = {8, 6, 8};
    vector<vector<int>> output = a.restoreMatrix(rowSum, colSum);
    /* Output:
    [ [ 0, 5, 0 ],
      [ 6, 1, 0 ],
      [ 2, 0, 8 ] ] 
    */
    cout << "[";
    for (int i = 0; i < output.size(); i++)
    {
        cout << endl
             << " [";
        for (int j = 0; j < output[0].size(); j++)
        {
            if (j == output[0].size() - 1)
                cout << output[i][j];
            else
                cout << output[i][j] << ", ";
        }
        cout << "]";
    }
    cout << endl
         << "]";
    return 0;
}