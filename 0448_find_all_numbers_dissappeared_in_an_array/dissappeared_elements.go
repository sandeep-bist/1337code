package main

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// Time: O(n)
// Space: O(n)
func findDisappearedNumbers(nums []int) []int {
	res := []int{}
	for i := range nums {
		index := abs(nums[i]) - 1
		if nums[index] > 0 {
			nums[index] *= -1
		}
	}
	for i := range nums {
		if nums[i] > 0 {
			res = append(res, i+1)
		}
	}
	return res
}
