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
