// Time: O(n * m)
// Space: O(n * m)
const orangesRotting = (grid) => {
  const queue = []
  let fresh = 0
  let m = grid.length
  let n = grid[0].length
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 2) queue.push([i, j])
      else if (grid[i][j] === 1) fresh++
    }
  }
  if (fresh === 0) return 0
  let count = 0
  while (queue.length) {
    const size = queue.length
    const directions = [
      [0, 1],
      [1, 0],
      [-1, 0],
      [0, -1],
    ]
    for (let i = 0; i < size; i++) {
      const [x, y] = queue.shift()
      for (let [r, c] of directions) {
        const xc = x + r
        const yc = y + c
        if (
          xc < 0 ||
          xc >= m ||
          yc < 0 ||
          yc >= n ||
          grid[xc][yc] === 0 ||
          grid[xc][yc] === 2
        )
          continue
        grid[xc][yc] = 2
        fresh--
        queue.push([xc, yc])
      }
    }
    count++
  }
  return fresh ? -1 : count - 1
}
