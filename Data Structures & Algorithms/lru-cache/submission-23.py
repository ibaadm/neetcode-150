class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}
        self.head = None
        self.tail = None

    def detach_node(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = None
        node.next = self.head

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        
        node = self.mp[key]
        if node != self.head:
            self.detach_node(node)
            self.head.prev = node
            self.head = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            if node != self.head:
                self.detach_node(node)
        else:
            node = Node(key, value)
            self.mp[key] = node

        if node != self.head:
            if self.head:
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:
                self.head = self.tail = node

        if len(self.mp) > self.cap:
            del self.mp[self.tail.key]
            if self.tail.prev:
                self.tail.prev.next = None
                self.tail.prev, self.tail = None, self.tail.prev
            else:
                self.tail = None