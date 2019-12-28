class ListNode {
  constructor(val) {
    this.val = val
    this.next = null
  }
}

/**
 * Given an array of integers, return indices of the two numbers
 * such that they add up to a specific target.
 * You may assume that each input would have exactly one solution,
 * and you may not use the same element twice.
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

const n1 = new ListNode(2)
const n2 = new ListNode(4)
const n3 = new ListNode(3)

n1.next = n2
n2.next = n3

const n4 = new ListNode(5)
const n5 = new ListNode(6)
const n6 = new ListNode(4)

n4.next = n5
n5.next = n6

let tmp = addTwoNumbers(n1, n4)
while (tmp) {
  console.log(tmp.val) // 7 0 8
  tmp = tmp.next
}
