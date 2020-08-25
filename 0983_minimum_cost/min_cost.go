// Time: O(m) where m is the max travel date
// Space: O(m)
func mincostTickets(days []int, costs []int) int {
	lastDay := days[len(days)-1]
	isTravelDay := make([]bool, lastDay+1)
	for _, day := range days {
		isTravelDay[day] = true
	}
	dp := make([]int, lastDay+1)
	for i := 1; i <= lastDay; i++ {
		if isTravelDay[i] == false {
			dp[i] = dp[i-1]
		} else {
			dp[i] = dp[i-1] + costs[0]
			dp[i] = min(dp[max(i-7, 0)]+costs[1], dp[i])
			dp[i] = min(dp[max(i-30, 0)]+costs[2], dp[i])
		}
	}
	return dp[lastDay]
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