/**
 * Time: O(n)
 * Space: O(n)
 */
const isHappy = n => {
  const s = new Set()
  while (true) {
    if (n === 1) return true
    let sum = n
      .toString()
      .split("")
      .reduce((a, b) => {
        a += Math.pow(+b, 2)
        return a
      }, 0)
    if (s.has(sum)) return false
    s.add(sum)
    n = sum
  }
}
