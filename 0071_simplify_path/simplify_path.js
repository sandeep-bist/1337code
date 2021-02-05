// Time: O(n)
// Space: O(n)
const simplifyPath = (path) => {
  const stack = []
  path.split('/').forEach((p) => {
    if (p === '..') {
      if (stack.length >= 0) {
        stack.pop()
      }
    } else if (p != '' && p != '.') {
      stack.push(p)
    }
  })
  return '/' + stack.join('/')
}
