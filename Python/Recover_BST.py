#https://leetcode.com/problems/recover-binary-search-tree/

class Solution:
    
    def inorder(self,root,arr):
        if root==None:
            return
        if root.left!=None:
            self.inorder(root.left,arr)
        arr.append(root.val)
        if root.right!=None:
            self.inorder(root.right,arr)
    
    def search(self,root,n1,n2):
        if root==None:
            return
        if root.left!=None:
            self.search(root.left,n1,n2)
        if root.val==n1:
            root.val=n2
        elif root.val==n2:
            root.val=n1
        if root.right!=None:
            self.search(root.right,n1,n2)
            
    
    def recoverTree(self, root: TreeNode) -> None:
        arr=[]
        self.inorder(root,arr)
        arr2=arr.copy()
        arr2.sort()
        n1=n2=0
        for i in range(len(arr)):
            if arr[i]!=arr2[i]:
                n1=arr2[i]
                n2=arr[i]
                break
        self.search(root,n1,n2)