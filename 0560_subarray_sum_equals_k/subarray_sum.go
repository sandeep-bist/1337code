package main

/**
 * Time: O(n)
 * Space: O(n)
 */
func subarraySum(nums []int, k int) int {
	ht := make(map[int]int)
	ht[0] = 1
	var total, res int
	for i := 0; i < len(nums); i++ {
		total += nums[i]
		val, ok := ht[total-k]
		if ok {
			res += val
		} else {
			res += 0
		}
		ht[total]++
	}
	return res
}

func main() {

}
