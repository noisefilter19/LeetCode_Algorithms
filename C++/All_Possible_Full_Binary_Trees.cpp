/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> allPossibleFBT(int n) {
        vector<TreeNode*> dp[21];
        
        TreeNode *temp;
        temp = new TreeNode;
        *temp = TreeNode();
        dp[1].push_back(temp);
        
        for(int i=3;i<20;i+=2)
        {
            for(int j=1; j<i; j+=2)
            {
                int ln = dp[j].size();
                int rn = dp[i-j-1].size();
                for(int k=0; k<ln; k++)
                {
                    for(int l=0; l<rn; l++)
                    {
                        temp = new TreeNode;
                        *temp = TreeNode(0, dp[j][k], dp[i-j-1][l]);
                        dp[i].push_back(temp);
                    }
                }
            }
        }
        
        return dp[n];
    }
};