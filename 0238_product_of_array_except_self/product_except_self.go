package main

/**
 * Time: O(n)
 * Space: O(n)
 */
func productExceptSelf(nums []int) []int {
	size := len(nums)
	res := make([]int, size)
	for i := 0; i < size; i++ {
		res[i] = 1
	}
	pi, pj := 1, 1
	for i := 0; i < size; i++ {
		j := size - 1 - i
		res[i] *= pi
		res[j] *= pj
		pi *= nums[i]
		pj *= nums[j]
	}
	return res
}

func main() {

}
