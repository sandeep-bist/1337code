import java.util.List;
import java.util.LinkedList;
import java.util.Arrays;
import java.util.Integer;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        return inOrder("", root);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] nodeArr = data.split(",");
        List<String> nodeList = new LinkedList<>(Arrays.asList(nodeArr));
        return build(nodeList);
    }

    private String inOrder(String output, TreeNode root) {
        if (root == null) {
            output += "null,";
        } else {
            output += root.val + ",";
            output = inOrder(output, root.left);
            output = inOrder(output, root.right);
        }
        return output;
    }

    private TreeNode build(List<String> nodeList) {
        if (nodeList.get(0).equals("null")) {
            nodeList.remove(0);
            return null;
        }
        TreeNode root = new TreeNode(Integer.valueOf(nodeList.get(0)));
        nodeList.remove(0);
        root.left = build(nodeList);
        root.right = build(nodeList);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// String tree = ser.serialize(root);
// TreeNode ans = deser.deserialize(tree);
// return ans;