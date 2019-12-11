/**
 * Given a sorted array and a target value, return the index if the target
 * is found. If not, return the index where it would be if it were inserted
 * in order.
 * You may assume no duplicates in the array.
 * @param   {number[]}  nums
 * @param   {number}    target
 * @return  {number}
 */
const searchInsert = (nums, target) => {
  let start = 0
  let end = nums.length - 1
  while (start <= end) {
    let mid = Math.floor((start + end) / 2)
    if (target > nums[mid]) start = mid + 1
    else if (target < nums[mid]) end = mid - 1
    else return mid
  }
  return start
}
