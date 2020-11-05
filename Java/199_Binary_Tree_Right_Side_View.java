/*

Problem No: 199. Binary Tree Right Side View
URI: https://leetcode.com/problems/binary-tree-right-side-view/
Logic:  A simple recursive implementation of level order traversal and the final RHS view is the last element of each of the level(which a new ArrayList)
*/

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
    public List<Integer> rightSideView(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        recurr(root,result,0);
        List<Integer> result_order = new ArrayList<>();
        for(int i=0;i<result.size();i++){
            result_order.add(result.get(i).get(result.get(i).size()-1));
        }
        return result_order;
    }
    public void recurr(TreeNode node,List<List<Integer>> result,int currDepth){
        if(node==null){
            return;
        }
        if(currDepth==result.size()){
            result.add(new ArrayList<>());
        }
        result.get(currDepth).add(node.val);
        recurr(node.left,result,currDepth+1);
        recurr(node.right,result,currDepth+1);
    }
}
