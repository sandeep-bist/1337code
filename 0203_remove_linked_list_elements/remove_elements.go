type ListNode struct {
	Val  int
	Next *ListNode
}

// Time: O(n)
// Space: O(n)
func removeElements(head *ListNode, val int) *ListNode {
	s := &ListNode{0, nil}
	curr := s
	for head != nil {
		if head.Val != val {
			curr.Next = head
			curr = curr.Next
		}
		head = head.Next
	}
	curr.Next = nil
	return s.Next
}