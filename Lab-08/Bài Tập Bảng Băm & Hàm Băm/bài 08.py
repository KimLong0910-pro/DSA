class HashTableQuadratic:
    def __init__(self, size=10):
        self.size = size
        self.bang = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        vi_tri = self.hash(key)

        for i in range(self.size):
            new_vi_tri = (vi_tri + i * i) % self.size

            if self.bang[new_vi_tri] is None:
                self.bang[new_vi_tri] = (key, value)
                return

    def get(self, key):
        vi_tri = self.hash(key)

        for i in range(self.size):
            new_vi_tri = (vi_tri + i * i) % self.size

            if self.bang[new_vi_tri] is None:
                return None

            if self.bang[new_vi_tri][0] == key:
                return self.bang[new_vi_tri][1]


bang = HashTableQuadratic()
bang.put("a", 1)
bang.put("b", 2)

print(bang.get("b"))
