/**
 * Time:    O(m * n)
 * Space:   O(1)
 * @param   {string[]} strings
 * @return  {string}
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
