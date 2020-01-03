/**
 * Given n non-negative integers a1, a2, ..., an , where each represents a
 * point at coordinate (i, ai). n vertical lines are drawn such that the
 * two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
 * together with x-axis forms a container, such that the container contains
 * the most water.
 * You may not slant the container and n is at least 2.
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

const arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
console.log(arr) // 49
