class ListNode {
  constructor(val) {
    this.val = val
    this.next = null
  }
}

/**
 * Given a linked list, remove the n-th node from the end of list and return
 * its head.
 * @param   {ListNode}  head
 * @param   {number}    n
 * @returns {ListNode}
 */
const removeNthNode = (head, n) => {
  let hare = head,
    tort = head
  while (n) {
    hare = hare.next
    n--
  }
  if (!hare) return hare.next
  while (hare.next) {
    tort = tort.next
    hare = hare.next
  }
  if (tort.next) tort.next = tort.next.next
  return head
}

const n1 = new ListNode(1)
const n2 = new ListNode(2)
const n3 = new ListNode(3)
const n4 = new ListNode(4)
const n5 = new ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

let tmp = removeNthNode(n1, 3)
while (tmp) {
  console.log(tmp.val) // 1, 2, 4, 5
  tmp = tmp.next
}
