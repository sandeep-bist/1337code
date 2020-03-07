/**
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
 * Time:    O(n * log(n) + 2**n)
 * Space:   O(n**2)
 * @param   {number[]}      candidates
 * @param   {number}        target
 */
const combinationSum = (candidates, target) => {
  const res = []
  candidates.sort((a, b) => a - b)
  dfs(candidates, [], 0, target, res)
  return res
}
