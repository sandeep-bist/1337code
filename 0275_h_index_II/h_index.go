package main

/**
 * Time: O(log(n))
 * Space: O(1)
 */
func hIndex(citations []int) int {
	size := len(citations)
	lo, hi := 0, size-1
	for lo <= hi {
		mid := (lo + hi) / 2
		mVal, c := citations[mid], size-mid
		if mVal == c {
			return c
		} else if mVal < c {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return size - lo
}

func main() {

}
