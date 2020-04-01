/**
 * Time: O(n)
 * Space: O(1)
 */
const singleNumber = nums => nums.reduce((a, b) => a ^ b, 0)
