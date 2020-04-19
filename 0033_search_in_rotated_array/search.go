package main

import "math"

/**
 * Time: O(log(n))
 * Space: O(1)
 */
func search(nums []int, target int) int {
	lo, hi := 0, len(nums)-1
	for lo <= hi {
		mid := (lo + hi) / 2
		if nums[mid] == target {
			return mid
		}
		var n int
		if (nums[lo] > nums[mid]) == (nums[lo] > target) {
			n = nums[mid]
		} else {
			if nums[0] > target {
				n = math.MinInt16
			} else {
				n = math.MaxInt16
			}
		}
		if n < target {
			lo = mid + 1
		} else if n > target {
			hi = mid - 1
		}
	}
	return -1
}

func main() {

}
