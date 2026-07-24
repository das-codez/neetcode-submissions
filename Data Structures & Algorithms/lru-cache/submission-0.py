class Node:
    def __init__(self, key, val):
        self.key,self.val = key,val
        self.next = self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}
        self.left,self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):
        nxt, prev = self.right, self.right.prev
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    def remove(self, node):
        nxt, prev = node.next, node.prev
        nxt.prev, prev.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.remove(self.nodes[key])
            self.insert(self.nodes[key])
            return self.nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(self.nodes[key])
        self.nodes[key] = Node(key, value)
        self.insert(self.nodes[key])
        if len(self.nodes) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.nodes[lru.key]
