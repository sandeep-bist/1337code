class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val
        this.next = next === undefined ? null : next
    }
}

const addTwoNumbers = (
    l1: ListNode | null,
    l2: ListNode | null,
    carry: number = 0
): ListNode | null => {
    if (!l1 && !l2 && !carry) {
        return null
    }
    const tmp: number = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry
    const node = new ListNode(tmp % 10)
    node.next = addTwoNumbers(
        l1 ? l1.next : null,
        l2 ? l2.next : null,
        tmp > 9 ? 1 : 0
    )
    return node
}
