class Codec {
public:
    TreeNode* decode(istringstream &s)
    {
        string curr;
        s>>curr;
        if(curr[0]=='#' || curr.empty())
            return NULL;
        TreeNode * root=new TreeNode(stoi(curr));
        root->left=decode(s);
        root->right=decode(s);
        return root;
    }
    
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string s;
        if(root==NULL)
            return "# ";
        s+=to_string(root->val)+" ";
        s+=serialize(root->left);
        s+=serialize(root->right);
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream s(data);
        return decode(s);
    }
};
