/**
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 * @param   {string[]} strings
 */
const longest_common_prefix = strings => {
  if (!strings.length) return ""
  const first = strings[0]
  for (let i = 0; i < first.length; i++) {
    let c = first[i]
    for (let str of strings)
      if (!str.length || str[i] != c) return first.slice(0, i)
  }
  return first
}

let strings = ["flower", "flow", "flight"] // fl
console.log(longest_common_prefix(strings))

strings = ["aa", "aa"] // aa
console.log(longest_common_prefix(strings))
