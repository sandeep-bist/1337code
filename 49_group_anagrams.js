/**
 * Given an array of strings, group anagrams together.
 * @param {string[]} strs
 * @return {string[][]}
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

const arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
console.log(groupAnagrams(arr))
/* [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]] */
