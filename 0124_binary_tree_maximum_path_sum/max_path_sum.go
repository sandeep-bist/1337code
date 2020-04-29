package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * Time: O(n)
 * Space: O(1)
 */
func maxPathSum(root *TreeNode) int {
	res := []int{math.MinInt16}
	helper(root, res)
	return res[0]
}

func helper(node *TreeNode, res []int) int {
	if node == nil {
		return 0
	}
	left := helper(node.Left, res)
	right := helper(node.Right, res)
	res[0] = max(res[0], left+node.Val+right)
	return max(node.Val+max(left, right), 0)
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {

}