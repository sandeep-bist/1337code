/**
 * Given an array with n objects colored red, white or blue, sort them
 * in-place so that objects of the same color are adjacent, with the
 * colors in the order red, white and blue.
 *
 * Here, we will use the integers 0, 1, and 2 to represent the color red,
 * white, and blue respectively.
 * Do not return anything, modify nums in-place instead.
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
