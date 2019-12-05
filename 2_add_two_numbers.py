class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    You are given two non-empty linked lists representing two non-negative
    integers. The digits are stored in reverse order and each of their nodes
    contain a single digit. Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the
    number 0 itself.
    """
    return add_two_numbers_helper(l1, l2, 0)


def add_two_numbers_helper(l1: ListNode, l2: ListNode, carry: int = 0) -> ListNode:
    if not l1 and not l2 and not carry:
        return None
    total = carry
    if l1:
        total += l1.val
        l1 = l1.next
    if l2:
        total += l2.val
        l2 = l2.next
    carry = 1 if total >= 10 else 0
    new_node = ListNode(total % 10)
    new_node.next = add_two_numbers_helper(l1, l2, carry)
    return new_node


def print_linked_list(head: ListNode):
    """
    Prints a linked list.
    """
    while head.next:
        print(head.val, end=" -> ")
        head = head.next
    print(head.val)


list_a = ListNode(2)
list_a.next = ListNode(4)
list_a.next.next = ListNode(3)

list_b = ListNode(5)
list_b.next = ListNode(6)
list_b.next.next = ListNode(4)


print_linked_list(addTwoNumbers(list_a, list_b))
# 7 -> 0 -> 8
