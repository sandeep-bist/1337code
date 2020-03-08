/**
 * Time:    O(m + n)
 * Space:   O(m + n)
 * @param   {string} paragraph
 * @param   {string[]} banned
 * @return  {string}
 */
const mostCommonWord = (paragraph, banned) => {
  const s = new Set(banned)
  const h = {}
  const p = paragraph.replace(/[^A-Za-z]/g, " ").split(" ")
  for (let w of p) {
    var temp = w.toLowerCase()
    if (!s.has(temp) && temp.length) {
      if (temp in h) h[temp]++
      else h[temp] = 1
    }
  }
  let maxCount = 0
  let maxKey = ""
  for (let [key, value] of Object.entries(h)) {
    if (value > maxCount) {
      maxCount = value
      maxKey = key
    }
  }
  return maxKey
}
