/**
 * Given n non-negative integers representing an elevation map where the
 * width of each bar is 1, compute how much water it is able to trap after
 * raining.
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

const arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
console.log(trap(arr)) // 6
