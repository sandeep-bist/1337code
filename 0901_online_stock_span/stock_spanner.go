package main

type Tuple struct {
	val    int
	weight int
}

type StockSpanner struct {
	stack []Tuple
}

func Constructor() StockSpanner {
	return StockSpanner{make([]Tuple, 0)}
}

/**
 * Time: O(q) where q is the number of calls to next()
 * Space: O(q)
 */
func (this *StockSpanner) Next(price int) int {
	weight := 1
	for len(this.stack) > 0 && this.stack[len(this.stack)-1].val <= price {
		weight += this.stack[len(this.stack)-1].weight
		this.stack = this.stack[:len(this.stack)-1]
	}
	this.stack = append(this.stack, Tuple{price, weight})
	return weight
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
