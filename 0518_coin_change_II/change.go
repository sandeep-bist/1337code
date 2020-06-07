package main

/**
 * Time: O(m * n)
 * Space: O(m * n)
 */
func change(amount int, coins []int) int {
	dp := make([]int, amount+1)
	dp[0] = 1
	for _, i := range coins {
		for j := 1; j < amount+1; j++ {
			if j >= i {
				dp[j] += dp[j-i]
			}
		}
	}
	return dp[amount]
}

func main() {

}
