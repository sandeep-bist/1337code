package main

import "math"

/**
 * Time: O(m * n)
 * Space: O(1)
 */
func countSquares(matrix [][]int) int {
	res := 0
	for r := 0; r < len(matrix); r++ {
		for c := 0; c < len(matrix[0]); c++ {
			if r > 0 && c > 0 && matrix[r][c] == 1 {
				matrix[r][c] = min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1]) + 1
			}
			res += matrix[r][c]
		}
	}
	return res
}

func min(nums ...int) int {
	res := math.MaxInt16
	for _, num := range nums {
		i := num
		if i < res {
			res = i
		}
	}
	return res
}

func main() {

}
