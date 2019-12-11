/**
 * Given a sorted array nums, remove the duplicates in-place such that each
 * element appear only once and return the new length.
 * Do not allocate extra space for another array, you must do this by
 * modifying the input array in-place with O(1) extra memory.
 * @param {number[]} nums
 * @return {number}
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

const arr = [1, 1, 2]
console.log(removeDuplicates(arr)) // 2
