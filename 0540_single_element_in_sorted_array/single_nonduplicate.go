package main

/**
 * Time: O(log(n))
 * Space: O(1)
 */
func singleNonDuplicate(nums []int) int {
	start, end := 0, len(nums)-1
	for start < end {
		mid := (start + end) / 2
		if mid&1 == 1 {
			mid--
		}
		if nums[mid] == nums[mid+1] {
			start = mid + 2
		} else {
			end = mid
		}
	}
	return nums[start]
}

func main() {

}
