/**
 * Time: O(m * n)
 * Space: O(1)
 * @param {number[][]} grid
 * @return {number}
 */
const minPathSum = grid => {
  const r = grid.length
  const c = grid[0].length
  for (i = 0; i < r; i++) {
    for (j = 0; j < c; j++) {
      if (!i && !j) continue
      const left = j > 0 ? grid[i][j - 1] : Number.MAX_SAFE_INTEGER
      const top = i > 0 ? grid[i - 1][j] : Number.MAX_SAFE_INTEGER
      grid[i][j] += Math.min(left, top)
    }
  }
  return grid[r - 1][c - 1]
}

