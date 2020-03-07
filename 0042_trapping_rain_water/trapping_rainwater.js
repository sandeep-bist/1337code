/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number[]} height
 * @returns {number}
 */
const trap = height => {
  let l = 0
  let r = height.length - 1
  let l_max = 0,
    r_max = 0,
    res = 0
  while (l < r) {
    if (height[l] < height[r]) {
      height[l] > l_max ? (l_max = height[l]) : (res += l_max - height[l])
      l++
    } else {
      height[r] > r_max ? (r_max = height[r]) : (res += r_max - height[r])
      r--
    }
  }
  return res
}
