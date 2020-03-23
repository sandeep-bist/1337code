/**
 * Time:        O(2**n)
 * Space:       O(n)
 * @param       {string[]} arr
 * @return      {number}
 */
const maxLength = arr => {
  const res = [0]
  dfs(arr, 0, "", res)
  return res[0]
}

const dfs = (arr, index, tmp, res) => {
  if (index == arr.length) {
    if (uniqChars(tmp) > res[0]) res[0] = tmp.length
    return
  }
  dfs(arr, index + 1, tmp, res)
  dfs(arr, index + 1, tmp + arr[index], res)
}

const uniqChars = str => {
  const s = new Set(str)
  if (str.length === s.size || 0) return str.length
  return -1
}
