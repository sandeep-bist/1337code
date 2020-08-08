// Time: O(n)
// Space: O(n)
const pathSum = (root, target) => {
  return preorder(root, 0, target)
}

const preorder = (node, currSum, target, cache = {}) => {
  if (!node) return 0
  currSum += node.val
  let res = cache[currSum - target] || 0
  if (currSum === target) res++
  cache[currSum] = cache[currSum] + 1 || 1
  res +=
    preorder(node.left, currSum, target, cache) +
    preorder(node.right, currSum, target, cache)
  cache[currSum] -= 1
  return res
}
