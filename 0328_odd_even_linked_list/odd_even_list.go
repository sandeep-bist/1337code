package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList(head *ListNode) *ListNode {
	odd := &ListNode{-1, nil}
	oddHead := odd
	even := &ListNode{-1, nil}
	evenHead := even
	for head != nil {
		odd.Next = head
		odd = odd.Next
		even.Next = head.Next
		even = even.Next
		if head.Next != nil {
			head = head.Next.Next
		} else {
			head = nil
		}
	}
	odd.Next = evenHead.Next
	return oddHead.Next
}

func main() {

}
