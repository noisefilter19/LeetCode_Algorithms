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
    public int sumRootToLeaf(TreeNode root) {
        int ans=0;
        Queue<Integer> v=new LinkedList<>();
        Queue<TreeNode> q=new LinkedList<>();
        v.add(root.val); q.add(root);
        while(!q.isEmpty())
        {
            int val=v.poll(); TreeNode p=q.poll();
            if(p.left==null && p.right==null) ans+=val;
            if(p.left!=null)
            {
                q.add(p.left);
                int nv=val*2+p.left.val;
                v.add(nv);
            }
            if(p.right!=null)
            {
                q.add(p.right);
                int nv=val*2+p.right.val;
                v.add(nv);
            }
        }
        return ans;
    }
}
