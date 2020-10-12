# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def inord(self, root, arr):
        if not root:
            return
        self.inord(root.left,arr)
        arr.append(str(root.val))
        self.inord(root.right,arr)
            
    def postord(self, root, arr):
        if not root:
            return
        self.postord(root.left,arr)
        self.postord(root.right,arr)
        arr.append(str(root.val))
        
        
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        inorder = []
        postorder = []
        
        self.inord(root, inorder)
        self.postord(root, postorder)
        
        string = ",".join(inorder) + '$' + ','.join(postorder)
        print(string)
        return string

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "$":
            return None
        inorder, postorder = data.split('$')
        inorder = [int(i) for i in inorder.split(',')]
        postorder = [int(i) for i in postorder.split(',')]
        
        return self.buildTree(inorder,postorder) 

        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorderDict = {}
        n = len(inorder)
        for i in range(n):
            inorderDict[inorder[i]] = i
        
        start = 0
        end = n-1
        
        self.head = None
        
        self.build(inorder, postorder, inorderDict, None, start, end, False, n-1)
        
        return self.head
    
    
    def build(self, inorder, postorder, inorderDict, head, start, end, left, rootIndex ):
        if start > end:
            return rootIndex
        nodeVal = postorder[rootIndex]
        index = inorderDict[nodeVal]
        rootIndex -= 1
        if head == None:
            head = TreeNode(nodeVal)
            self.head = head
        elif left:
            head.left = TreeNode(nodeVal)
            head = head.left
        else:
            head.right = TreeNode(nodeVal)
            head = head.right
        
        rootIndex = self.build(inorder, postorder, inorderDict, head, index+1, end, False, rootIndex)
        rootIndex = self.build(inorder, postorder, inorderDict, head, start, index-1, True, rootIndex)
        
        return rootIndex

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
