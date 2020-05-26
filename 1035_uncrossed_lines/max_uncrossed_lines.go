package main

/**
 * Time: O(m * n)
 * Space: O(m * n)
 */
func maxUncrossedLines(A []int, B []int) int {
	// bottom-up approach
	m, n := len(A), len(B)
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}
	for r := m - 1; r >= 0; r-- {
		for c := n - 1; c >= 0; c-- {
			if A[r] == B[c] {
				dp[r][c] = dp[r+1][c+1] + 1
			} else {
				dp[r][c] = max(dp[r][c+1], dp[r+1][c])
			}
		}
	}
	return dp[0][0]
}

func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}

func main() {

}
