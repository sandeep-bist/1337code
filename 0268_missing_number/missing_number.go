package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func missingNumber(nums []int) int {
	missing := len(nums)
	for i, e := range nums {
		missing ^= i ^ e
	}
	return missing
}

func main() {

}
