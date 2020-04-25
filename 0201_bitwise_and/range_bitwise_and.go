package main

/**
 * Time: O(1)
 * Space: O(1)
 */
func rangeBitwiseAnd(m int, n int) int {
	shifts := 0
	for m < n {
		m >>= 1
		n >>= 1
		shifts++
	}
	return m << uint(shifts)
}

func main() {

}
