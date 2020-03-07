/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number[]} height
 * @return  {number}
 */
const maxArea = height => {
  let l = 0,
    r = height.length - 1
  let max = Number.MIN_SAFE_INTEGER
  while (l < r) {
    let min = Math.min(height[l], height[r])
    max = Math.max(max, min * (r - l))
    height[r] > height[l] ? l++ : r--
  }
  return max
}
