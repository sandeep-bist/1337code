package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Time: O(log(n))
// Space: O(1)
func closestValue(root *TreeNode, target float64) int {
	res := root.Val
	for root != nil {
		if math.Abs(target-float64(root.Val)) < math.Abs(target-float64(res)) {
			res = root.Val
		}
		if target > float64(root.Val) {
			root = root.Right
		} else {
			root = root.Left
		}
	}
	return res
}

func main() {

}
