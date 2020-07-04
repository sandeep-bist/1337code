package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Time: O(n)
// Space: O(n)
func levelOrderBottom(root *TreeNode) [][]int {
	res := make([][]int, 0)
	if root == nil {
		return res
	}
	traverse(root, 0, &res)
	reverse(&res)
	return res
}

func traverse(node *TreeNode, level int, res *[][]int) {
	if len(*res) == level {
		*res = append(*res, []int{})
	}
	(*res)[level] = append((*res)[level], node.Val)
	if node.Left != nil {
		traverse(node.Left, level+1, res)
	}
	if node.Right != nil {
		traverse(node.Right, level+1, res)
	}

}

func reverse(res *[][]int) {
	for i, j := 0, len(*res)-1; i < j; i, j = i+1, j-1 {
		(*res)[i], (*res)[j] = (*res)[j], (*res)[i]
	}
}

func main() {

}
