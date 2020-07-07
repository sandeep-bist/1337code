package main

func islandPerimeter(grid [][]int) int {
	r, c, res := len(grid), len(grid[0]), 0
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			if grid[i][j] == 1 {
				res += 4
				if i > 0 && grid[i-1][j] == 1 {
					res -= 2
				}
				if j > 0 && grid[i][j-1] == 1 {
					res -= 2
				}
			}
		}
	}
	return res
}

func main() {

}
