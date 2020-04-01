package main

/**
 * Time: O(n)
 * Space: O(1)
 */
func singleNumber(nums []int) int {
	res := 0
	for _, i := range nums {
		res ^= i
	}
	return res
}

func main() {

}
