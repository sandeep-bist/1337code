package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func canJump(nums []int) bool {
	m := 0
	for i, e := range nums {
		if i > m {
			return false
		}
		m = max(m, i+e)
	}
	return true
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}