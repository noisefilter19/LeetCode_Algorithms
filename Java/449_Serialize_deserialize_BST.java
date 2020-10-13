//Leetcode link : https://leetcode.com/problems/serialize-and-deserialize-bst/

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null)
            return "";
        return bfs(root);
    }

    // returns a comma separated BFS traversal of the tree.
    public String bfs(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        List<String> vals = new ArrayList<String>();
        q.add(root);

        while (!q.isEmpty()) {
            TreeNode node = q.remove();
            vals.add(String.valueOf(node.val));
            if (node.left != null)
                q.add(node.left);
            if (node.right != null)
                q.add(node.right);
        }
        return String.join(",", vals);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.length() < 1)
            return null;

        String[] vals;
        vals = data.split(",");
        TreeNode root = new TreeNode(Integer.valueOf(vals[0]));

        for (int i = 1; i < vals.length; i++) {
            int val = Integer.valueOf(vals[i]);
            insertIntoBST(root, val);
        }

        return root;
    }

    // inserts a value into the BST at the correct position.
    public void insertIntoBST(TreeNode root, int val) {
        TreeNode node = root;
        TreeNode prev = root;
        while (node != null) {
            prev = node;
            if (val > node.val)
                node = node.right;
            else
                node = node.left;
        }

        node = new TreeNode(val);
        if (val > prev.val)
            prev.right = node;
        else
            prev.left = node;
    }
}
