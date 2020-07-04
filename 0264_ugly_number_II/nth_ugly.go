package main

import "math"

// Time: O(n)
// Space: O(n)
func nthUglyNumber(n int) int {
	res := []int{1}
	u2, u3, u5 := 0, 0, 0
	for n > 1 {
		umin2, umin3, umin5 := 2*res[u2], 3*res[u3], 5*res[u5]
		ugly := min(umin2, umin3, umin5)
		res = append(res, ugly)
		if ugly == umin2 {
			u2++
		}
		if ugly == umin3 {
			u3++
		}
		if ugly == umin5 {
			u5++
		}
		n--
	}
	return res[len(res)-1]
}

func min(nums ...int) int {
	res := math.MaxInt32
	for _, num := range nums {
		if num < res {
			res = num
		}
	}
	return res
}

func main() {

}
