package main

import "math"

// Time: O(n)
// Space: O(1)
func maxProfit(prices []int) int {
	hold, notHold, notHoldCoolDown := math.MinInt16, 0, math.MinInt16
	for _, p := range prices {
		hold = max(hold, notHold-p)
		notHold = max(notHold, notHoldCoolDown)
		notHoldCoolDown = hold + p
	}
	return max(notHold, notHoldCoolDown)
}

func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}

func main() {

}
