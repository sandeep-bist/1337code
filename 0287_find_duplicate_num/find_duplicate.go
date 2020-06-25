package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func findDuplicate(nums []int) int {
	t, h := nums[0], nums[0]
	for {
		t = nums[t]
		h = nums[nums[h]]
		if t == h {
			break
		}
	}
	h = nums[0]
	for t != h {
		h = nums[h]
		t = nums[t]
	}
	return h
}

func main() {

}
