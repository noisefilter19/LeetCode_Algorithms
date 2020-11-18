#include <bits/stdc++.h> 
using namespace std; 
  
class node  
{  
    public: 
    int data;  
    node* left, *right;  
};  
node *lca(node* root, int n1, int n2)  
{  
    if (root == NULL) return NULL;   
    if (root->data > n1 && root->data > n2)  
        return lca(root->left, n1, n2);  
    if (root->data < n1 && root->data < n2)  
        return lca(root->right, n1, n2);  
  
    return root;  
}  
node* newNode(int data)  
{  
    node* Node = new node(); 
    Node->data = data;  
    Node->left = Node->right = NULL;  
    return(Node);  
}  
int main()  
{  
    node *root = newNode(20);  
    root->left = newNode(8);  
    root->right = newNode(22);  
    root->left->left = newNode(4);  
    root->left->right = newNode(12);  
    root->left->right->left = newNode(10);  
    root->left->right->right = newNode(14);  
  
    int n1 = 10, n2 = 14;  
    node *t = lca(root, n1, n2);  
    cout << "LCA of " << n1 << " and " << n2 << " is " << t->data<<endl;  
  
    n1 = 14, n2 = 8;  
    t = lca(root, n1, n2);  
    cout<<"LCA of " << n1 << " and " << n2 << " is " << t->data << endl;  
  
    n1 = 10, n2 = 22;  
    t = lca(root, n1, n2);  
    cout << "LCA of " << n1 << " and " << n2 << " is " << t->data << endl;  
    return 0;  
}  