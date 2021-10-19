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
    int find(TreeNode* root,int& cnt,int k)
    {
        if(root==NULL)
            return -1;
        int kth=find(root->left,cnt,k);
        if(kth!=-1)
        {
            return kth;
        }
        cnt+=1;
        if(cnt==k)
        {
            return root->val;
        }
        return find(root->right,cnt,k);
    }
    int kthSmallest(TreeNode* root, int k) {
        int cnt=0;
        return find(root,cnt,k);
    }
};
