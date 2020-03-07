class ListNode {
  constructor(val) {
    this.val = val
    this.next = null
  }
}

/**
 * Time:    O(n)
 * Space:   O(1)
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
