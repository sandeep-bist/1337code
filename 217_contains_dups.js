/**
 * Given an array of integers, find if the array contains any duplicates.
 * Your function should return true if any value appears at least twice in
 * the array, and it should return false if every element is distinct.
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = nums => {
  const set = new Set(nums)
  return set.size !== nums.length
}

const arr = [1, 2, 3, 1]
console.log(containsDuplicate(arr)) // true

const arr2 = [1, 2, 3]
console.log(containsDuplicate(arr2)) // false

const arr3 = []
console.log(containsDuplicate(arr3)) // false
