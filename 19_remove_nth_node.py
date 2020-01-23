class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    Given a linked list, remove the n-th node from the end of list and return
    its head.
    """
    hare = tort = head
    while n:
        hare = hare.next
        n -= 1
    if not hare:
        # Hare has reached end of list, will need to delete head.
        return head.next
    while hare.next:
        tort = tort.next
        hare = hare.next
    if tort.next:
        tort.next = tort.next.next
    return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

temp = remove_nth_from_end(n1, 5)
while temp:
    print(temp.val)  # 2, 3, 4, 5
    temp = temp.next
