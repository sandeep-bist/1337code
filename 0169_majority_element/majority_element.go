package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func majorityElement(nums []int) int {
	count, candidate := 0, 0
	for _, n := range nums {
		if count == 0 {
			candidate = n
		}
		if n == candidate {
			count++
		} else {
			count--
		}
	}
	return candidate
}

func main() {

}
