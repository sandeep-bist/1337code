package main

/**
 * Time: O(log(n))
 * Space: O(1)
 */
func searchInsert(nums []int, target int) int {
	i, j := 0, len(nums)-1
	for i <= j {
		mid := (i + j) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			j = mid - 1
		} else {
			i = mid + 1
		}
	}
	return i
}

func main() {

}
