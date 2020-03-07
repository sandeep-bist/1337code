/**
 * Time:    O(n)
 * Space:   O(1)
 * @param   {number[]} nums
 * @return  {number}
 */
const rob = nums => {
  let prev_max = 0,
    curr_max = 0
  nums.forEach(el => {
    let tmp = Math.max(el + prev_max, curr_max)
    prev_max = curr_max
    curr_max = tmp
  })
  return curr_max
}
