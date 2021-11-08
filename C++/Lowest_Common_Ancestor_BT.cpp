class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
        if(root==NULL){
            return NULL;
        }
        
        if(root==p || root==q){   // if any of the node is root node then that node will be LCA
            return root;
        }
        
        TreeNode* lTree=lowestCommonAncestor(root->left,p,q);   //call on left subtree
        TreeNode* rTree=lowestCommonAncestor(root->right,p,q);  // call on right subtree
        if(lTree && rTree){   // if both subtrees contain node then root will be the commom anscestor
            return root;
        }else if(lTree){
            return lTree;
        }else if(rTree){
            return rTree;
        }else{
            return NULL;
        }
    }
};
