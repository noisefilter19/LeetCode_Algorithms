"""Python program to check if a node exists
in a binary tree."""

# A Binary Tree Node
# Utility function to create a new tree node
class newNode:

    # Constructor to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to traverse the tree in preorder
# and check if the given node exists in it
def ifNodeExists(node, key):

    if (node == None):
        return False

    if node.data == key:
        return True

    """ then recur on left sutree """
    res1 = ifNodeExists(node.left, key)
    # node found, no need to look further
    if res1:
        return True

    """ node is not found in left, 
    so recur on right subtree """
    res2 = ifNodeExists(node.right, key)

    return res2

# Driver Code
if __name__ == '__main__':
    root = newNode(0)
    root.left = newNode(1)
    root.left.left = newNode(3)
    root.left.left.left = newNode(7)
    root.left.right = newNode(4)
    root.left.right.left = newNode(8)
    root.left.right.right = newNode(9)
    root.right = newNode(2)
    root.right.left = newNode(5)
    root.right.right = newNode(6)

    key = 4

    if ifNodeExists(root, key):
        print("YES" )
    else:
        print("NO")
