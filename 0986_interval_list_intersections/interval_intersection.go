package main

/**
 * Time: O(m + n)
 * Space: O(m + n)
 */
func intervalIntersection(A [][]int, B [][]int) [][]int {
	n, m, i, j := len(A), len(B), 0, 0
	res := make([][]int, 0)
	for i < n && j < m {
		if A[i][1] >= B[j][0] && A[i][0] <= B[j][1] {
			tmp := []int{max(A[i][0], B[j][0]), min(A[i][1], B[j][1])}
			res = append(res, tmp)
		}
		if A[i][1] < B[j][1] {
			i++
		} else {
			j++
		}
	}
	return res
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}