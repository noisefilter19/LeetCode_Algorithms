
//https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) 
    {
        if(root == NULL)
            return NULL;
        
        if(root==p || root ==q)
            return root;
        TreeNode *l = lowestCommonAncestor(root->left, p, q);
        TreeNode *r = lowestCommonAncestor(root->right, p, q);
        
        // If both of the above calls return Non-NULL, then one key 
        // is present in once subtree and other is present in other, 
        // So this node is the LCA 
        if(l && r)
            return root;
        
        // Otherwise check if left subtree or right subtree is LCA 
        if(l)
            return l;
        else
            return r;
            
    }
};