package main

// Time: O(1)
// Space: O(1)
func hammingDistance(x int, y int) int {
	xor, res := x^y, 0
	for xor != 0 {
		res++
		xor &= xor - 1
	}
	return res
}

func main() {

}
