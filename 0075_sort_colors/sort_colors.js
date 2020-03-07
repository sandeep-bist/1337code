/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number[]} nums
 * @return
 */
const sortColors = nums => {
  let p0, c, p2
  p0 = c = 0
  p2 = nums.length - 1
  while (c <= p2) {
    if (nums[c] === 0) [nums[c++], nums[p0++]] = [nums[p0], nums[c]]
    else if (nums[c] === 2) [nums[c], nums[p2--]] = [nums[p2], nums[c]]
    else c++
  }
}
