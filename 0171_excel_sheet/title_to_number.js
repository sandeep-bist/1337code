// Time: O(n)
// Space: O(n)
const titleToNumber = (s) =>
  s.split('').reduce((a, b) => {
    return a * 26 + b.charCodeAt() - 64
  }, 0)
