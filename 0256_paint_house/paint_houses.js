/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number[][]}    costs
 * @returns {number}
 */
const minCost = costs => {
  if (!costs.length) return 0
  for (let i = 1; i < costs.length; i++) {
    let prev = costs[i - 1]
    costs[i][0] += Math.min(prev[1], prev[2])
    costs[i][1] += Math.min(prev[0], prev[2])
    costs[i][2] += Math.min(prev[0], prev[1])
  }
  return Math.min(...costs[costs.length - 1])
}
