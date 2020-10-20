import java.util.*;

class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }

    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}

class Solution {
    // Time: O(n + m) where m is the number of edges
    // Space: O(n)
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        Map<Node, Node> visited = new HashMap<Node, Node>();
        visited.put(node, new Node(node.val, new ArrayList()));
        LinkedList<Node> queue = new LinkedList<>();
        queue.add(node);
        while (!queue.isEmpty()) {
            Node curr = queue.remove();
            for (Node neighbor : curr.neighbors) {
                if (!visited.containsKey(neighbor)) {
                    queue.add(neighbor);
                    visited.put(neighbor, new Node(neighbor.val, new ArrayList()));
                }
                visited.get(curr).neighbors.add(visited.get(neighbor));
            }
        }
        return visited.get(node);
    }
}