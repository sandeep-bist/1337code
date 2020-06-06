package main

import (
	"time"
	"math/rand"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

type Solution struct {
	sums []int
}

func Constructor(w []int) Solution {
	sums := []int{0}
	sum := 0
	for i := 0; i < len(w); i++ {
		sum += w[i]
		sums = append(sums, sum)
	}
	return Solution{
		sums: sums,
	}
}

/**
 * Time: O(log(n))
 * Space: O(n)
 */
func (this *Solution) PickIndex() int {
	r := rand.Intn(this.sums[len(this.sums)-1])
	left, right := 0, len(this.sums)-1
	for left <= right {
		mid := (left + right) / 2
		if this.sums[mid] <= r && r < this.sums[mid+1] {
			return mid
		} else if this.sums[mid] > r {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return -1
}

func main() {

}