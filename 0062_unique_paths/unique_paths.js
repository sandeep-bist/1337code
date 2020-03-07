/**
 * Time:    O(m * n)
 * Space:   O(m * n)
 * @param   {number} m
 * @param   {number} n
 * @returns {number}
 */
const uniquePaths = (m, n) => {
  const dp = []
  let tmp = m
  while (tmp--) dp.push(Array(n).fill(1))
  for (let i = 1; i < m; i++)
    for (let j = 1; j < n; j++) dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
  return dp[m - 1][n - 1]
}
