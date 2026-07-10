class HashTable:
    def __init__(self, size=4):
        self.size = size
        self.dem = 0
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        if self.dem / self.size > 0.75:
            self.rehash()

        vi_tri = self.hash(key)
        self.buckets[vi_tri].append((key, value))
        self.dem += 1

    def rehash(self):
        cu = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.dem = 0

        for bucket in cu:
            for key, value in bucket:
                self.put(key, value)


bang = HashTable()

bang.put("a", 1)
bang.put("b", 2)
bang.put("c", 3)
bang.put("d", 4)

print(bang.size)
