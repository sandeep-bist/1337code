/**
 * Time: O(n)
 * Space: O(1)
 */
const missingNumber = (nums) => nums.reduce((a, b, i) => a ^ b ^ i, nums.length)
