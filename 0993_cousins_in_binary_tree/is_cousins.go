package main

import "container/list"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * Time: O(n)
 * Space: O(n)
 */
func isCousins(root *TreeNode, x int, y int) bool {
	q := list.New()
	q.PushBack(root)
	var siblings, cousins bool
	for q.Len() > 0 {
		siblings, cousins = false, false
		tmpLen := q.Len()
		for i := 0; i < tmpLen; i++ {
			popped := q.Front()
			q.Remove(popped)
			if popped.Value == nil {
				siblings = false
			} else {
				if popped.Value.(*TreeNode).Val == x || popped.Value.(*TreeNode).Val == y {
					if cousins == false {
						siblings, cousins = true, true
					} else {
						return !siblings
					}
				}
				if popped.Value.(*TreeNode).Left != nil {
					q.PushBack(popped.Value.(*TreeNode).Left)
				}
				if popped.Value.(*TreeNode).Right != nil {
					q.PushBack(popped.Value.(*TreeNode).Right)
				}
				q.PushBack(nil)
			}
		}
		if cousins == true {
			return false
		}
	}
	return false
}

func main() {

}