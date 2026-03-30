class Node:
    def __init__(self, key, val):
        self.prev = self.next = None
        self.key, self.val = key, val

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity 
        self.left, self.right = Node(0, 0), Node(0 ,0)
        self.right.prev = self.left
        self.left.next = self.right       

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            

