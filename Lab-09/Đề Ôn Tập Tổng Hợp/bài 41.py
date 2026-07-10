class Node:
    def __init__(self, key, gia_tri):
        self.key = key
        self.gia_tri = gia_tri
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, suc_chua):
        self.suc_chua = suc_chua
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_first(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.add_first(node)

        return node.gia_tri

    def put(self, key, gia_tri):
        if key in self.cache:
            node = self.cache[key]
            node.gia_tri = gia_tri
            self.remove(node)
            self.add_first(node)

        else:
            if len(self.cache) == self.suc_chua:
                xoa = self.tail.prev
                self.remove(xoa)
                del self.cache[xoa.key]

            node = Node(key, gia_tri)
            self.cache[key] = node
            self.add_first(node)


cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
print(f"Get(1): {cache.get(1)}")
cache.put(3, 30)
print(f"Get(2): {cache.get(2)}")
cache.put(4, 40)
print(f"Get(1): {cache.get(1)}")
print(f"Get(3): {cache.get(3)}")
print(f"Get(4): {cache.get(4)}")
