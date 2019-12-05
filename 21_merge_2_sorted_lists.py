class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists and return it as a new list. The new list
    should be made by splicing together the nodes of the first two lists.
    """
    head = curr = ListNode(None)
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return head.next


def print_linked_list(head: ListNode):
    """
    Prints a linked list.
    """
    while head.next:
        print(head.val, end=", ")
        head = head.next
    print(head.val)


list_a = ListNode(1)
list_a.next = ListNode(2)
list_a.next.next = ListNode(4)

list_b = ListNode(1)
list_b.next = ListNode(3)
list_b.next.next = ListNode(4)

print_linked_list(merge_two_lists(list_a, list_b))
# 1, 1, 2, 3, 4, 4
