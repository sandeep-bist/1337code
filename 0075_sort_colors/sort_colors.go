package main

/**
 * Time:    O(n)
 * Space:   O(1)
 */
func sortColors(nums []int) {
	c0, c1, c2 := 0, 0, len(nums)-1
	for c1 <= c2 {
		if nums[c1] == 0 {
			nums[c0], nums[c1] = nums[c1], nums[c0]
			c0++
			c1++
		} else if nums[c1] == 2 {
			nums[c2], nums[c1] = nums[c1], nums[c2]
			c2--
		} else {
			c1++
		}
	}
}

func main() {

}
