/**
 * Time: O(n)
 * Space: O(n)
 */
const firstUniqChar = (s) => {
  const counter = s.split("").reduce((a, b) => {
    if (b in a) a[b]++
    else a[b] = 1
    return a
  }, {})
  for (let i = 0; i < s.length; i++) {
    if (counter[s[i]] === 1) return i
  }
  return -1
}
