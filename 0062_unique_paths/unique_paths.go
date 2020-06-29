package main

/**
 * Time: O(m * n)
 * Space: O(m * n)
 */
func uniquePaths(m int, n int) int {
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, m)
	}
	for r := 0; r < n; r++ {
		for c := 0; c < m; c++ {
			if r == 0 || c == 0 {
				dp[r][c] = 1
			} else {
				dp[r][c] = dp[r-1][c] + dp[r][c-1]
			}
		}
	}
	return dp[n-1][m-1]
}

func main() {

}
