package main

// This is the BinaryMatrix's API interface.
// You should not implement it, or speculate about its implementation
type BinaryMatrix struct {
   Get(int, int) int
   Dimensions() []int
}

/**
 * Time: O(n)
 * Space: O(1)
 */
func leftMostColumnWithOne(binaryMatrix BinaryMatrix) int {
	dimensions := binaryMatrix.Dimensions()
	r, c := dimensions[0], dimensions[1]
	res := -1
	row, col := 0, c-1
	for col >= 0 && row < r {
		if binaryMatrix.Get(row, col) == 1 {
			res = col
			col--
		} else {
			row++
		}
	}
	return res
}

func main() {

}