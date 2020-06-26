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
func sumNumbers(root *TreeNode) int {
	return dfs(root, 0)
}

func dfs(node *TreeNode, curr int) int {
	if node != nil {
		curr = curr*10 + node.Val
		if node.Left == nil && node.Right == nil {
			return curr
		}
		return dfs(node.Left, curr) + dfs(node.Right, curr)
	}
	return 0
}

func main() {

}
