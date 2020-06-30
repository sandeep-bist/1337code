package main

import "math"

/**
 * Time: O(n * h/2) where h is the height of the N-ary tree
 * Space: O(sqrt(n) * h)
 */
func numSquares(n int) int {
	if n < 2 {
		return n
	}
	i, res := 1, 0
	squares := make([]int, 0)
	for i*i <= n {
		squares = append(squares, i*i)
		i++
	}
	q := make(map[int]bool)
	q[n] = true
	for len(q) != 0 {
		res++
		tmp := make(map[int]bool)
		for val := range q {
			for j := 0; j < len(squares); j++ {
				square := squares[j]
				if val == square {
					return res
				} else if j > square {
					break
				} else {
					tmp[val-square] = true
				}
			}
		}
		q = tmp
	}
	return res
}

func isSquare(n int) bool {
	s := int(math.Sqrt(float64(n)))
	return s*s == n
}

/**
 * Time: O(sqrt(n))
 * Space: O(1)
 */
func numSquaresMath(n int) int {
	if n == 0 {
		return 0
	}
	if isSquare(n) {
		return 1
	}
	for (n & 3) == 0 {
		n >>= 2
	}
	if (n & 7) == 7 {
		return 4
	}
	s := int(math.Sqrt(float64(n)))
	for i := 1; i <= s; i++ {
		if isSquare(n - i*i) {
			return 2
		}
	}
	return 3
}

func main() {

}
