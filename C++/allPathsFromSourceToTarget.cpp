#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    void helper(vector<vector<int>> &graph, vector<vector<int>> &ans, vector<int> &v, int u)
    {
        v.push_back(u);
        if (u == graph.size() - 1)
            ans.push_back(v);
        for (int x : graph[u])
        {
            helper(graph, ans, v, x);
        }
        v.pop_back();
    }
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>> &graph)
    {

        vector<vector<int>> ans;
        vector<int> v;
        helper(graph, ans, v, 0);
        return ans;
    }
};