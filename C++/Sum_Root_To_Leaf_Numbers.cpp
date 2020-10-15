
//https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution {
public:
    int ans = 0; //ans stores the sum of all root-to-leaf paths

    int sumNumbers(TreeNode* root) {
        solve(root, 0);
        return ans;
    }
    
    void solve(TreeNode* node, int cur){ //helper function
        if(node == NULL) return;
        cur = cur*10;
        cur += node->val;
        
        if(node->left == NULL && node->right == NULL){ //node is a leaf
            ans += cur;
        }else{
            solve(node->left, cur);
            solve(node->right, cur);
        }
    }
};
