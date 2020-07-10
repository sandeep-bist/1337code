package main

type Node struct {
	Val   int
	Prev  *Node
	Next  *Node
	Child *Node
}

// Time: O(n)
// Space: O(n)
func flatten(root *Node) *Node {
	if root == nil {
		return nil
	}
	s := Node{0, nil, nil, nil}
	stack := []*Node{root}
	prev := &s
	for len(stack) > 0 {
		curr := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		prev.Next = curr
		curr.Prev = prev
		if curr.Next != nil {
			stack = append(stack, curr.Next)
			curr.Next = nil
		}
		if curr.Child != nil {
			stack = append(stack, curr.Child)
			curr.Child = nil
		}
		prev = curr
	}
	s.Next.Prev = nil
	return s.Next
}

func main() {

}
