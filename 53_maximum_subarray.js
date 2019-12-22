/**
 * Given an integer array nums, find the contiguous subarray (containing
 * at least one number) which has the largest sum and return its sum.
 * @param   {number[]}  nums
 * @returns {number}
 */
const maxSubArray = nums => {
  if (!nums.length) return 0
  for (let i = 1; i < nums.length; i++)
    if (nums[i - 1] > 0) nums[i] = nums[i] + nums[i - 1]
  return Math.max(...nums)
}

let arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
console.log(maxSubArray(arr)) // 6

arr = []
console.log(maxSubArray([])) // 0
