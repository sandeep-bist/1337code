package main

/**
 * Time: O(n)
 * Space: O(n)
 */
func findMaxLength(nums []int) int {
	indexes := make(map[int]int)
	indexes[0] = -1
	res, tmp := 0, 0
	for i, e := range nums {
		if e == 1 {
			tmp++
		} else {
			tmp--
		}
		index, ok := indexes[tmp]
		if ok {
			res = max(res, i-index)
		} else {
			indexes[tmp] = i
		}
	}
	return res
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {

}
