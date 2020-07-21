func exist(board [][]byte, word string) bool {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if board[i][j] == word[0] {
				if dfs(board, 0, i, j, word) {
					return true
				}
			}
		}
	}

	return false
}

func dfs(board [][]byte, index int, r int, c int, word string) bool {
	if index == len(word) {
		return true
	}
	if r < 0 || r >= len(board) || c < 0 || c >= len(board[0]) || board[r][c] != word[index] {
		return false
	}
	tmp := board[r][c]
	board[r][c] = '#'
	var found bool
	found = (dfs(board, index+1, r+1, c, word) ||
		dfs(board, index+1, r, c+1, word) ||
		dfs(board, index+1, r-1, c, word) ||
		dfs(board, index+1, r, c-1, word))
	board[r][c] = tmp
	return found
}