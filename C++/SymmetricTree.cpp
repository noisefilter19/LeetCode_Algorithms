/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool checkSym(TreeNode* lft, TreeNode* ryt){
        if(lft == NULL && ryt == NULL){
            return true;
        }
        else if((lft != NULL && ryt == NULL) || (lft == NULL && ryt != NULL)){
            return false;
        }
        else if(lft->val != ryt->val){
            return false;
        }
        return checkSym(lft->left, ryt->right) & checkSym(lft->right, ryt->left);
    }
    
    bool isSymmetric(TreeNode* root) {
        if(root == NULL){
            return true;
        }
         
        return checkSym(root->left, root->right);
    }
};