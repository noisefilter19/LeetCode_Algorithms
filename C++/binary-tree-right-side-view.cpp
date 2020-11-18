/**
 * Solution to Binary Tree Right Side View at LeetCode in C++
 *
 * author: thepanshuyadav
 * ref: https://leetcode.com/problems/binary-tree-right-side-view */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        queue<TreeNode*> q;
        vector<int> ans;
        if(!root) {
            return ans;
        }
        else {
            q.push(root);
            q.push(NULL);
        }
        
        
        while(q.size()>1) {
            TreeNode* node = q.front();
            q.pop();
            if(q.front() == NULL) {
                int v = node->val;
                ans.push_back(v);
            }
            if(node == NULL) {
                q.push(NULL);
            }
            else {
                if(node->left) {
                    q.push(node->left);
                }
                if(node->right) {
                    q.push(node->right);
                }
            }
        }
        return ans;
    }
};
