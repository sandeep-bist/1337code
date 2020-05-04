package main

import "math/bits"

/**
 * Time: O(1)
 * Space: O(1)
 */
func findComplement(N int) int {
	if N == 0 {
		return 1
	}
	return (1 << uint(bits.Len(uint(N)))) - 1 - N
}

func main() {

}
