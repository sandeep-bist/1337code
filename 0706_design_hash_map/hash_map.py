class ListNode:
    def __init__(self, key: int, value: int):
        self.val = (key, value)
        self.next = None


class MyHashMap:
    def __init__(self):
        self.hm = [None for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        """
        Value will always be non-negative.
        """
        node = ListNode(key, value)
        h = self.get_hash(key)
        if not self.hm[h]:
            self.hm[h] = node
        else:
            prev, curr = None, self.hm[h]
            while curr:
                if curr.val[0] == key:
                    # Update
                    curr.val = (key, value)
                    return
                prev = curr
                curr = curr.next
            prev.next = node

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key.
        """
        h = self.get_hash(key)
        if not self.hm[h]:
            return -1
        curr = self.hm[h]
        while curr:
            if curr.val[0] == key:
                return curr.val[1]
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key
        if this map contains a mapping for the key.
        """
        h = self.get_hash(key)
        if not self.hm[h]:
            return
        prev = curr = self.hm[h]
        # head
        if curr.val[0] == key:
            self.hm[h] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.val[0] == key:
                    prev.next = curr.next
                    return
                prev = prev.next
                curr = curr.next

    def get_hash(self, num: int) -> int:
        return (num * 31) % 1000
