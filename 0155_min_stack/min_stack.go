package main

type Stack struct {
	val int
	min int
}

type MinStack struct {
	s []Stack
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(x int) {
	if len(this.s) == 0 {
		this.s = append(this.s, Stack{x, x})
	} else {
		minVal := this.GetMin()
		this.s = append(this.s, Stack{x, Min(x, minVal)})
	}
}

func (this *MinStack) Pop() {
	this.s = this.s[:len(this.s)-1]
}

func (this *MinStack) Top() int {
	return this.s[len(this.s)-1].val
}

func (this *MinStack) GetMin() int {
	if len(this.s) > 0 {
		return this.s[len(this.s)-1].min
	}
	return 0
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */

func main() {

}
