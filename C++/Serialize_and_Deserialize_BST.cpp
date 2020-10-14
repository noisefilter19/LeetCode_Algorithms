//https://leetcode.com/problems/serialize-and-deserialize-bst/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
    void serialize_help(TreeNode* root,string &serialized)
    {
        if(!root)
        {
            serialized+=" NULL";
            return;
        }
        
        serialized+=" "+to_string(root->val);

        serialize_help(root->left,serialized);

        serialize_help(root->right,serialized);
    
       
        
    }
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        
        string serialized = "";
        
        serialize_help(root,serialized);
        
        return serialized;
    
        
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        
        stringstream strs(data);
        TreeNode *root = buildBST(strs);
        return root;
        
    }
    
    TreeNode* buildBST(stringstream &strs)
    {
        string s;
        strs>>s;
        
        if(s=="NULL") return NULL;
        
        TreeNode *node = new TreeNode(stoi(s));        
        node->left = buildBST(strs);
        node->right = buildBST(strs);
        
        return node;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec* ser = new Codec();
// Codec* deser = new Codec();
// string tree = ser->serialize(root);
// TreeNode* ans = deser->deserialize(tree);
// return ans;
