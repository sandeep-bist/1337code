class ListNode {
  constructor(val) {
    this.val = val
    this.next = null
  }
}

/**
 * Time:    O(m + n)
 * Space:   O(m + n)
 * @param   {ListNode}  l1
 * @param   {ListNode}  l2
 * @param   {number}    carry
 * @return  {ListNode}
 */
const addTwoNumbers = (l1, l2, carry = 0) => {
  if (!l1 && !l2 && !carry) return null
  const tmp = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry
  const node = new ListNode(tmp % 10)
  node.next = addTwoNumbers(
    l1 ? l1.next : null,
    l2 ? l2.next : null,
    tmp > 9 ? 1 : 0
  )
  return node
}
