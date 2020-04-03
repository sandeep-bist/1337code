/**
 * Time: O(n)
 * Space: O(1)
 */
const maxSubArray = nums => {
  if (!nums.length) return 0
  for (let i = 1; i < nums.length; i++)
    if (nums[i - 1] > 0) nums[i] = nums[i] + nums[i - 1]
  return Math.max(...nums)
}
