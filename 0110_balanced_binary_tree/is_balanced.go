package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * Time: O(n)
 * Space: O(n)
 */
func isBalanced(root *TreeNode) bool {
	return dfs(root) != -1
}

func dfs(node *TreeNode) int {
	if node == nil {
		return 0
	}
	left := dfs(node.Left)
	if left == -1 {
		return -1
	}
	right := dfs(node.Right)
	if right == -1 {
		return -1
	}
	if abs(left-right) > 1 {
		return -1
	}
	return max(left, right) + 1
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}

func main() {

}
