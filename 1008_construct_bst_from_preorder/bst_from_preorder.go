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
func bstFromPreorder(preorder []int) *TreeNode {
	stack := []*TreeNode{}
	root := TreeNode{preorder[0], nil, nil}
	stack = append(stack, &root)
	for i := 1; i < len(preorder); i++ {
		curr := preorder[i]
		last := stack[len(stack)-1]
		if curr < stack[len(stack)-1].Val {
			last.Left = &TreeNode{curr, nil, nil}
			stack = append(stack, last.Left)
		} else {
			for len(stack) > 0 && stack[len(stack)-1].Val < curr {
				last = stack[len(stack)-1]
				stack = stack[:len(stack)-1]
			}
			last.Right = &TreeNode{curr, nil, nil}
			stack = append(stack, last.Right)
		}
	}
	return &root
}

func main() {

}
