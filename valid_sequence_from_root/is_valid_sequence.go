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
func isValidSequence(root *TreeNode, arr []int) bool {
	return dfs(root, 0, arr)
}

func dfs(node *TreeNode, depth int, arr []int) bool {
	if node == nil || depth >= len(arr) || node.Val != arr[depth] {
		return false
	}
	if node.Right == nil && node.Left == nil {
		return depth+1 == len(arr)
	}
	return dfs(node.Left, depth+1, arr) || dfs(node.Right, depth+1, arr)
}

func main() {

}
