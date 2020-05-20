package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * Time: O(h + k) where h is the height of the tree
 * Space: O(h + k)
 */
func kthSmallest(root *TreeNode, k int) int {
	stack := make([]*TreeNode, 0)
	for {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		k--
		if k == 0 {
			return root.Val
		}
		root = root.Right
	}
}

func main() {

}
