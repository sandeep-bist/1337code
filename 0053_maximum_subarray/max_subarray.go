package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func maxSubArray(nums []int) int {
	maxSoFar, maxCurr := nums[0], nums[0]
	for _, i := range nums[1:] {
		if (i + maxCurr) > i {
			maxCurr = i + maxCurr
		} else {
			maxCurr = i
		}
		maxSoFar = max(maxSoFar, maxCurr)
	}
	return maxSoFar
}

func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}

func main() {

}
