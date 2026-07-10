class HashTable:
    def __init__(self, size=4):
        self.size = size
        self.dem = 0
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        if (self.dem + 1) / self.size > 0.75:
            self.rehash()

        vi_tri = self.hash(key)

        for i, (k, _) in enumerate(self.buckets[vi_tri]):
            if k == key:
                self.buckets[vi_tri][i] = (key, value)
                return

        self.buckets[vi_tri].append((key, value))
        self.dem += 1

    def get(self, key):
        vi_tri = self.hash(key)

        for k, value in self.buckets[vi_tri]:
            if k == key:
                return value

        return None

    def rehash(self):
        bang_cu = self.buckets

        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.dem = 0

        for bucket in bang_cu:
            for key, value in bucket:
                self.put(key, value)


bang = HashTable()

bang.put("a", 1)
bang.put("b", 2)
bang.put("c", 3)
bang.put("d", 4)

print(f"Kích thước bảng: {bang.size}")
print(f"Giá trị của 'c': {bang.get('c')}")