/**
 * Depth-first search.
 * @param   {string[][]}    matrix
 * @param   {number}        r
 * @param   {number}        c
 * @param   {number}        index
 * @param   {string}        word
 * @returns {boolean}
 */
const dfs = (matrix, r, c, index, word) => {
  if (index === word.length) return true
  if (
    r < 0 ||
    r >= matrix.length ||
    c < 0 ||
    c >= matrix[0].length ||
    matrix[r][c] !== word[index]
  )
    return false
  const tmp = matrix[r][c]
  matrix[r][c] = " "
  const found =
    dfs(matrix, r + 1, c, index + 1, word) ||
    dfs(matrix, r, c + 1, index + 1, word) ||
    dfs(matrix, r - 1, c, index + 1, word) ||
    dfs(matrix, r, c - 1, index + 1, word)
  matrix[r][c] = tmp
  return found
}

/**
 * Given a 2D board and a word, find if the word exists in the grid.
 * The word can be constructed from letters of sequentially adjacent cell,
 * where "adjacent" cells are those horizontally or vertically neighboring.
 * The same letter cell may not be used more than once.
 * @param   {string[][]}        matrix
 * @param   {string}            word
 * @returns {boolean}
 */
const exist = (matrix, word) => {
  for (let i = 0; i < matrix.length; i++)
    for (let j = 0; j < matrix[0].length; j++)
      if (matrix[i][j] === word[0] && dfs(matrix, i, j, 0, word)) return true
  return false
}

const matrix = [
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"]
]
console.log(exist(matrix, "ABCCED")) // true
console.log(exist(matrix, "ABCD")) // false
