/**
 * A robot is located at the top-left corner of a m x n grid (marked 'Start'
 * in the diagram below).
 * The robot can only move either down or right at any point in time. The
 * robot is trying to reach the bottom-right corner of the grid (marked
 * 'Finish' in the diagram below).
 * How many possible unique paths are there?
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

console.log(uniquePaths(3, 2)) // 3
