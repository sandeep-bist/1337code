/**
 * Time:    O(m * n)
 * Space:   O(m * n)
 * @param   {character[][]} grid
 * @return  {number}
 */
const numIslands = grid => {
  let islands = 0
  for (let i = 0; i < grid.length; i++)
    for (let j = 0; j < grid[0].length; j++)
      if (grid[i][j] === "1") islands += dfs(grid, i, j)
  return islands
}

/**
 * @param   {character[][]} grid
 * @param   {number}        row
 * @param   {number}        col
 * @returns {number}
 */
const dfs = (grid, row, col) => {
  if (
    row < 0 ||
    col < 0 ||
    row >= grid.length ||
    col >= grid[0].length ||
    grid[row][col] === "0"
  )
    return (grid[row][col] = "0")
  dfs(grid, row - 1, col)
  dfs(grid, row, col - 1)
  dfs(grid, row + 1, col)
  dfs(grid, row, col + 1)
  return 1
}
