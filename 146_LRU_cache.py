from collections import OrderedDict

# first solution with doubly-linked lists


class ListNode:
    def __init__(self, key: int, value: str):
        """
        ListNode constructor.
        """
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        """
        LRU cache.
        """
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.hash_map = {}

    def get(self, key: int) -> int:
        """
        Gets the value stored at given key. Moves key to the front of cache.
        """
        node = self.hash_map.get(key)
        if not node:
            return -1
        if node != self.head:
            self.move_to_front(node)
        return node.value

    def put(self, key: int, value: str):
        """
        Inserts a key, value pair into the cache if it does not exist.
        Otherwise, updates the current key.
        Moves key to the front of the cache.
        """
        if key in self.hash_map:
            node = self.hash_map.get(key)
            node.value = value
            if node != self.head:
                return self.move_to_front(node)
        if self.is_full():
            self.evict()
        self.insert_to_head(key, value)

    def is_full(self):
        """
        Determines if cache is full or not.
        """
        return self.size >= self.capacity

    def insert_to_head(self, key: int, value: str):
        """
        Inserts a node to the head of the cache.
        """
        node = ListNode(key, value)
        self.hash_map[key] = node
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node
        self.size += 1

    def move_to_front(self, node: ListNode):
        """
        Moves a node in the cache to the front.
        """
        prev_node = node.prev
        next_node = node.next
        if node == self.tail:
            self.tail = prev_node
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def evict(self):
        """
        Removes the least recently used node from the end of the cache.
        """
        del self.hash_map[self.tail.key]
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size -= 1

    def __str__(self):
        """
        String representation.
        """
        res = ""
        curr = self.head
        while curr:
            res += str(curr.key)
            if curr.next:
                res += " <-> "
            curr = curr.next
        return res


# second solution with ordered dicts

class LRUCacheOD:
    def __init__(self, Capacity):
        """
        LRUCache constructor with Ordered Dicts.
        """
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        Gets the value stored at given key. Moves key to the front of cache.
        """
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        """
        Inserts a key, value pair into the cache if it does not exist.
        Otherwise, updates the current key.
        Moves key to the front of the cache.
        """
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


obj = LRUCache(2)
obj.put(2, "1")
obj.put(2, "2")
print(obj)  # 2
print(obj.get(2))  # 2
obj.put(1, "1")
print(obj)  # 1 <-> 2
obj.put(4, "1")
print(obj)  # 4 <-> 1
print(obj.get(2))  # -1

obj = LRUCache(3)
obj.put(3, "cherries")
print(obj)  # 3
obj.put(4, "dikon")
obj.put(5, "eggplants")
obj.put(6, "fruits")
print(obj)  # 6 <-> 5 <-> 4
obj.put(1, "apples")
print(obj.get(1))  # apples
print(obj)  # 1 <-> 6 <-> 5
print(obj.get(6))  # fruits
print(obj.get(2))  # -1
print(obj)  # 6 <-> 1 <-> 5
obj.put(7, "grapefruit")
print(obj)  # 7 <-> 6 <-> 1
print(obj.get(6))  # fruits
print(obj)  # 6 <-> 7 <-> 1
