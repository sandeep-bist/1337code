/**
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of
 * islands. An island is surrounded by water and is formed by connecting
 * adjacent lands horizontally or vertically. You may assume all four edges
 * of the grid are all surrounded by water.
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
 * Depth-first search.
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
    return
  grid[row][col] = "0"
  dfs(grid, row - 1, col)
  dfs(grid, row, col - 1)
  dfs(grid, row + 1, col)
  dfs(grid, row, col + 1)
  return 1
}

/*
Input:
11110
11010
11000
00000

Output: 1

Input:
11000
11000
00100
00011

Output: 3
*/
