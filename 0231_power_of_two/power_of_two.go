package main

/**
 * Time: O(1)
 * Space: O(1)
 */
func isPowerOfTwo(n int) bool {
	if n == 0 {
		return false
	}
	return (n & (n - 1)) == 0
}

func main() {

}
