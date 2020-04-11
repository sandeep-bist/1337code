package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * Time: O(n)
 * Space: O(1)
 */
func diameterOfBinaryTree(root *TreeNode) int {
	m := 0
	depth(root, &m)
	return m
}

func depth(node *TreeNode, m *int) int {
	if node == nil {
		return 0
	}
	left, right := depth(node.Left, m), depth(node.Right, m)
	*m = max(left+right, *m)
	return max(left, right) + 1
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {

}
