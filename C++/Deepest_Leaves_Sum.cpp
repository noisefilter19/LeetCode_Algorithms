// https://leetcode.com/problems/deepest-leaves-sum/
// 1302 | Deepest Leaves Sum | C++

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
	// Function to calculate maximum depth
    int maxDepth(TreeNode* node)  
    {  
    if (node == NULL)  
        return 0;   
    int lDepth = maxDepth(node->left);  
    int rDepth = maxDepth(node->right);  
    // compare depth of both child of the node
    if (lDepth > rDepth)  
        return(lDepth + 1);  
    else return(rDepth + 1);    
    }  
    
    int deepestLeavesSum(TreeNode* root) {
        if(root==NULL)
            return 0;
        // Using BFS for traversal
        queue<pair<TreeNode*,int>>q;
        q.push({root,1});
        int d=maxDepth(root);
        int sum=0;
        while(!q.empty()){
            TreeNode* temp=q.front().first;
            int level=q.front().second;
            q.pop();
            if(temp->left!=NULL)
                q.push({temp->left,level+1});
            if(temp->right!=NULL)
                q.push({temp->right,level+1});
            // If level of node is equal to maximum Depth,sum it up
            if(level==d)
                sum+=temp->val;
        }
        return sum;
    }
};
