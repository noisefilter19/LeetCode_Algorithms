//PROBLEM-LINK=https://leetcode.com/problems/binary-tree-inorder-traversal/
//ISSUE-LINK=https://github.com/noisefilter19/LeetCode_Algorithms/issues/795
 //Definition for a binary tree node.
 /*struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };*/
 //Recursive solution passing all test cases
class Solution {
    //take an vector of integers for storing output
    vector<int> soln;
public:
    vector<int> inorderTraversal(TreeNode* root) {
        //If root is NULL, return.
        if(root==NULL)
        
            return{} ;
        //recursively traverse and puch values into ans via the left part of tree
inorderTraversal(root->left);
        //push the value of root
soln.push_back(root->val);
        //recursively traverse and puch values into ans via the right part of tree
inorderTraversal(root->right);
        //return the vector
return soln;
    }
};
