/**
 * Depth-first search.
 * @param   {number[]}      nums
 * @param   {number[]}      sub
 * @param   {number}        index
 * @param   {number}        target
 * @param   {number[][]}    res
 */
const dfs = (nums, sub, index, target, res) => {
  if (!target) {
    res.push([...sub])
    return
  }
  for (let i = index; i < nums.length; i++) {
    if (nums[i] > target) break
    sub.push(nums[i])
    dfs(nums, sub, i, target - nums[i], res)
    sub.pop()
  }
}

/**
 * Given a set of candidate numbers (candidates) (without duplicates) and a
 * target number (target), find all unique combinations in candidates where
 * the candidate numbers sums to target.
 * The same repeated number may be chosen from candidates unlimited number
 * of times.
 * @param   {number[]}      candidates
 * @param   {number}        target
 */
const combinationSum = (candidates, target) => {
  const res = []
  candidates.sort((a, b) => a - b)
  dfs(candidates, [], 0, target, res)
  return res
}

const arr = [3, 12, 9, 11, 6, 7, 8, 5, 4]
console.log(combinationSum(arr, 15))
/*  
  [[3, 3, 3, 3, 3],
  [3, 3, 3, 6],
  [3, 3, 4, 5],
  [3, 3, 9],
  [3, 4, 4, 4],
  [3, 4, 8],
  [3, 5, 7],
  [3, 6, 6],
  [3, 12],
  [4, 4, 7],
  [4, 5, 6],
  [4, 11],
  [5, 5, 5],
  [6, 9],
  [7, 8]] */
