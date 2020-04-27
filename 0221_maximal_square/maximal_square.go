package main

import (
	"math"
)

/**
 * Time: O(m * n)
 * Space: O(1)
 */
func maximalSquare(matrix [][]byte) int {
	res := 0
	for r := 0; r < len(matrix); r++ {
		for c := 0; c < len(matrix[0]); c++ {
			if matrix[r][c] == '1' && r > 0 && c > 0 {
				matrix[r][c] = min(matrix[r-1][c],
								   matrix[r-1][c-1],
								   matrix[r][c-1]) + 1
			}
			res = max(res, int(matrix[r][c]-'0'))
		}
	}
	return res * res
}

func min(nums ...byte) byte {
	res := math.MaxInt16
	for _, num := range nums {
		i := int(num)
		if i < res {
			res = i
		}
	}
	return byte(res)
}

func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}

func main() {

}
