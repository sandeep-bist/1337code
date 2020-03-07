class Node:
    def __init__(self, val: int, next: 'Node', random: 'Node'):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Node) -> Node:
    """
    Time: O(2n)
    Space: O(n)
    """
    hash_map = {}
    curr = head
    while curr:
        node = Node(curr.val, None, None)
        hash_map[id(curr)] = node
        curr = curr.next
    curr = head
    while curr:
        clone = hash_map.get(id(curr))
        clone.next = hash_map.get(id(curr.next))
        clone.random = hash_map.get(id(curr.random))
        curr = curr.next
    return hash_map.get(id(head))
