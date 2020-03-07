/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number[]} nums
 * @return  {number}
 */
const removeDuplicates = nums => {
  s = new Set()
  let i = 0
  while (i < nums.length) {
    let curr = nums[i]
    if (s.has(curr)) nums.splice(i, 1)
    else {
      s.add(curr)
      i++
    }
  }
  return i
}