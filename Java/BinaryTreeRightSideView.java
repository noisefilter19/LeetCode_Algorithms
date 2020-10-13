/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    /*
    idea: we want the rightmost node of each level of our tree, so
    we can go in order of right then left child, and if we already have
    a tree of height > than what it would be by adding this node, we
    know we must have already accepted a node from this level of our tree.
    
    Otherwise, we can add the current node, increment our height so far
    and go right then left on this node.  
    */
    
    //variable for height so far we have found for rightmost node
    int TreeHeight=0;
    
    //list of integers we will return
    List<Integer>rightSide=new ArrayList<Integer>();
    
    public List<Integer> rightSideView(TreeNode root) {
        //call our recursive method with our root at height = 0
        getRightMost(0,root);
        return rightSide;
    }
    public void getRightMost(int height, TreeNode r){
        //base case: if we go beyond a leaf, we cannot go further, so return
        if(r==null)
            return;
        
        //if TreeHeight>height, we already found a node at level = TreeHeight further right than this one
        if(TreeHeight>height){
            //so we try going right then left on its children
            getRightMost(height+1,r.right);
            getRightMost(height+1,r.left);
        }
        //otherwise, this is the rightmost node for this level
        else{        
        //so we add to our list
        rightSide.add(r.val);
        //increase our maximum height so far
        TreeHeight++;
        //and recursively call this method on the right and then left child of our current node
        getRightMost(height+1,r.right);
        getRightMost(height+1,r.left);
            }
    }
}
