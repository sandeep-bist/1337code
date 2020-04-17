package main

/**
 * Time: O(m * n)
 * Space: O(m * n)
 */
func numIslands(grid [][]byte) int {
	count := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == '1' {
				count += dfs(grid, i, j)
			}
		}
	}
	return count
}

func dfs(grid [][]byte, r int, c int) int {
	if r < 0 || c < 0 || r >= len(grid) || c >= len(grid[0]) || grid[r][c] == '0' {
		return 0
	}
	grid[r][c] = '0'
	dfs(grid, r+1, c)
	dfs(grid, r, c+1)
	dfs(grid, r-1, c)
	dfs(grid, r, c-1)
	return 1
}

func main() {

}
