package main

/**
 * Time: O(m * n)
 * Space: O(1)
 */
func minPathSum(grid [][]int) int {
    const MaxInt = int(^uint(0) >> 1)
    r := len(grid)
    c := len(grid[0])
    for i := 0; i < r; i++ {
        for j := 0; j < c; j++ {
            if i == 0 && j == 0 {
                continue
            }
            var top, left int
            if i > 0 {
                top = grid[i - 1][j]
            } else {
                top = MaxInt
            }
            if j > 0 {
                left = grid[i][j - 1]
            } else {
                left = MaxInt
            }
            grid[i][j] = grid[i][j] + min(top, left)
        }
    }
    return grid[r - 1][c - 1]
}

func min(x, y int) int {
    if (x < y) {
        return x
    }
    return y
}

func main() {
	
}