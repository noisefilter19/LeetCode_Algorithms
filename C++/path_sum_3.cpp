// Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

// The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


// /**
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
        
        int ans=0;
        void solve(TreeNode* root, int tg){
                if(!root) return ;
                
                if(tg==root->val) ans++;
                
                solve(root->left, tg-root->val);
                solve(root->right, tg-root->val);
                
        }
        
        
    int pathSum(TreeNode* root, int targetSum) {
            
            if(!root) return 0;
            
            solve(root,targetSum);
            
            pathSum(root->left,targetSum);
            pathSum(root->right,targetSum);
            
            return ans;
        
    }
};
