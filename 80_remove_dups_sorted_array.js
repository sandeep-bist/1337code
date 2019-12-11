/**
 * Given a sorted array nums, remove the duplicates in-place such that
 * duplicates appeared at most twice and return the new length.
 * Do not allocate extra space for another array, you must do this by
 * modifying the input array in-place with O(1) extra memory.
 * @param   {number[]}  nums
 * @return  {number}
 */
const removeDuplicates = nums => {
  const count = {}
  let i = 0
  while (i < nums.length) {
    let curr = nums[i]
    if (count[curr] > 1) {
      nums.splice(i, 1)
    } else {
      count[curr] = count[curr] + 1 || 1
      i++
    }
  }
  return i
}

const arr = [1, 1, 1, 2, 2, 3]
console.log(removeDuplicates(arr)) // 5
