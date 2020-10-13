//LeetCode Problem link - https://leetcode.com/problems/deepest-leaves-sum/

class Solution {
public:
    int maxDepth(TreeNode* node)  
    {  
    if (node == NULL)  
        return 0;   
    int lDepth = maxDepth(node->left);  
    int rDepth = maxDepth(node->right);  
    if (lDepth > rDepth)  
        return(lDepth + 1);  
    else return(rDepth + 1);    
    }  
    
    int deepestLeavesSum(TreeNode* root) {
        if(root==NULL)
            return 0;
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
            if(level==d)
                sum+=temp->val;
        }
        return sum;
    }
};
