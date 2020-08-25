// Time: O(m) where m is the max travel date
// Space: O(m)
const mincostTickets = (days, costs) => {
  const lastDay = days[days.length - 1]
  const isTravelDay = new Set()
  days.forEach((day) => isTravelDay.add(day))
  const dp = new Array(lastDay + 1).fill(0)
  for (let i = 1; i <= lastDay; i++) {
    if (!isTravelDay.has(i)) {
      dp[i] = dp[i - 1]
    } else {
      dp[i] = dp[i - 1] + costs[0]
      dp[i] = Math.min(dp[Math.max(i - 7, 0)] + costs[1], dp[i])
      dp[i] = Math.min(dp[Math.max(i - 30, 0)] + costs[2], dp[i])
    }
  }
  return dp[lastDay]
}
