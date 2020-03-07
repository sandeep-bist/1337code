/**
 * Time:    O(m * n * n * log(n))
 * Space:   O(m * n * n)
 * @param   {string[]}    strs
 * @return  {string[][]}
 */
const groupAnagrams = strs => {
  const map = {}
  for (let s of strs) {
    const sorted = s
      .split("")
      .sort()
      .join("")
    if (!(sorted in map)) map[sorted] = [s]
    else map[sorted].push(s)
  }
  return Object.values(map)
}
