package main

/**
 * Time: O(n)
 * Space: O(n)
 */
func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	oldColor := image[sr][sc]
	if oldColor == newColor {
		return image
	}
	dfs(image, sr, sc, oldColor, newColor)
	return image
}

func dfs(image [][]int, sr int, sc int, oldColor int, newColor int) {
	if sr < 0 || sc < 0 || sr >= len(image) || sc >= len(image[0]) {
		return
	}
	if image[sr][sc] == oldColor {
		image[sr][sc] = newColor
		dfs(image, sr+1, sc, oldColor, newColor)
		dfs(image, sr, sc+1, oldColor, newColor)
		dfs(image, sr-1, sc, oldColor, newColor)
		dfs(image, sr, sc-1, oldColor, newColor)
	}
}

func main() {

}
