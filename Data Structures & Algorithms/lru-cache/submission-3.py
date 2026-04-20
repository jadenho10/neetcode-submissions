class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {} # key: Node(k, v)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    def add(self, node):
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.next, node.prev = self.right, prev
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        
