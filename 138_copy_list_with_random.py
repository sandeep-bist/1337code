class Node:
    def __init__(self, val: int, next: 'Node', random: 'Node'):
        """
        Node constructor.
        """
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Node) -> Node:
    """
    A linked list is given such that each node contains an additional random
    pointer which could point to any node in the list or null.
    Return a deep copy of the list.
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


n1 = Node(1, None, None)
n2 = Node(2, None, None)
n3 = Node(3, None, None)
n4 = Node(4, None, None)
n5 = Node(5, None, None)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n1.random = n3
n2.random = n5
n3.random = n2
n4.random = n1
n5.random = n4

curr = n1
node = copy_random_list(n1)
while curr and node:
    print(
        f"original - val: {curr.val}, random: {curr.random.val}, \
            id: {id(curr)}")
    print(
        f"clone    - val: {node.val}, random: {node.random.val}, \
            id: {id(node)}")
    print("---------------")
    curr = curr.next
    node = node.next

"""
original - val: 1, random: 3, id: 140625485020176
clone    - val: 1, random: 3, id: 140625485020560
---------------
original - val: 2, random: 5, id: 140625485020304
clone    - val: 2, random: 5, id: 140625485020624
---------------
original - val: 3, random: 2, id: 140625485020368
clone    - val: 3, random: 2, id: 140625485020688
---------------
original - val: 4, random: 1, id: 140625485020432
clone    - val: 4, random: 1, id: 140625485020752
---------------
original - val: 5, random: 4, id: 140625485020496
clone    - val: 5, random: 4, id: 140625485020816
---------------
"""
