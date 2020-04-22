/**
 * Time: O(n)
 * Space: O(n)
 */
const subarraySum = (nums, k) => {
  const cache = { 0: 1 }
  return nums.reduce(
    (obj, curr) => {
      obj.total += curr
      const subtotal = obj.total
      obj.res += cache[subtotal - k] || 0
      cache[subtotal] = ++cache[subtotal] || 1
      return obj
    },
    { total: 0, res: 0 }
  ).res
}
