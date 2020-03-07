/**
 * Time:    O(n)
 * Space:   O(n)
 * @param   {number[]} nums
 * @return  {boolean}
 */
const containsDuplicate = nums => {
  const set = new Set(nums)
  return set.size !== nums.length
}
