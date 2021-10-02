//problem link:https://leetcode.com/problems/maximum-matrix-sum/



class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {

        long long ans = 0;

        long long mimin = 1e12;
        long long c = 0;
        int t = 0;

        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = 0; j < matrix[0].size(); j++)
            {
                ans += abs(matrix[i][j]);
                mimin = min(mimin, (long long)abs(matrix[i][j]));
                if (matrix[i][j] == 0) t = 1;

                if (matrix[i][j] < 0)
                    c++;
            }
        }

        cout << endl;
        if (c % 2 == 0 || t)
            return ans;
        else
            return ans - 2 * mimin;
    }
};