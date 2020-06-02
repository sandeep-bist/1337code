package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * Time: O(1)
 * Space: O(1)
 */
func deleteNode(node *ListNode) {
	next := node.Next
	node.Val = next.Val
	node.Next = next.Next
}

func main() {

}
