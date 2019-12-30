/**
 * Given an array nums of n integers, are there elements a, b, c in nums such
 * that a + b + c = 0? Find all unique triplets in the array which gives the
 * sum of zero.
 * The solution set must not contain duplicate triplets.
 * @param   {number[]}      nums
 * @return  {number[][]}
 */
const threeSum = nums => {
  nums.sort((a, b) => a - b)
  const res = []
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue
    let j = i + 1
    let k = nums.length - 1
    while (j < k) {
      let sum = nums[i] + nums[j] + nums[k]
      if (sum > 0) k--
      else if (sum < 0) j++
      else {
        res.push([nums[i], nums[j], nums[k]])
        while (j < k && nums[j] === nums[j + 1]) j++
        while (j < k && nums[k] === nums[k - 1]) k--
        j++
        k--
      }
    }
  }
  return res
}

const arr = [-1, 0, 1, 2, -1, -4]
console.log(threeSum(arr)) // [[-1,-1,2],[-1,0,1]]
