package main

import "math"

/**
 * Time: O(n)
 * Space: O(1)
 */
func maxSubarraySumCircular(A []int) int {
	maxCurr, maxSoFar := math.MinInt16, math.MinInt16
	minCurr, minSoFar := 0, 0
	total := 0
	for _, a := range A {
		maxCurr = max(a, maxCurr+a)
		maxSoFar = max(maxSoFar, maxCurr)
		minCurr = min(a, minCurr+a)
		minSoFar = min(minSoFar, minCurr)
		total += a
	}
	if maxSoFar < 0 {
		return maxSoFar
	}
	return max(maxSoFar, total-minSoFar)
}

func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x <= y {
		return x
	}
	return y
}

func main() {

}
