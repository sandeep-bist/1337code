/**
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
 * Time:    O(n * 4**L) where L is the length of the word
 * Space:   O(L)
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
