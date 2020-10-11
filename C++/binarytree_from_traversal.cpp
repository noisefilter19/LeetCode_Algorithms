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
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        TreeNode *root = new TreeNode(preorder[0]);
        for(int i = 1; i < preorder.size(); i++)
        {
            insertNode(root, preorder[i]);
        }
        return root;
    }
    void insertNode(TreeNode *head, int val)
    {
        if(head->val < val)
        {
            if(head->right != nullptr)
                insertNode(head->right, val);
            else 
                head->right = new TreeNode(val);
        }
        if(head->val > val)
        {
            if(head->left != nullptr)
                insertNode(head->left, val);
            else
                head->left = new TreeNode(val);
        }
        
    }
};