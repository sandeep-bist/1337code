/**
 * Given an array of integers, return indices of the two numbers
 * such that they add up to a specific target.
 * You may assume that each input would have exactly one solution,
 * and you may not use the same element twice.
 * @param   {number[]}  nums
 * @param   {number}    target
 * @return  {number[]}
 */
const twoSum = (nums, target) => {
  const map = {}
  for (let i in nums) {
    let curr = nums[i]
    let compliment = target - curr
    if (map[compliment] !== undefined) return [map[compliment], i]
    else map[curr] = i
  }
  return []
}

console.log(twoSum([2, 7, 11, 15], 9)) // [0, 1]
