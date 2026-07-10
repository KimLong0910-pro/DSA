class BloomFilter:
    def __init__(self, size=10):
        self.size = size
        self.bits = [0] * size

    def hash1(self, gia_tri):
        return hash(gia_tri) % self.size

    def hash2(self, gia_tri):
        return (hash(gia_tri) * 7) % self.size

    def add(self, gia_tri):
        self.bits[self.hash1(gia_tri)] = 1
        self.bits[self.hash2(gia_tri)] = 1

    def contains(self, gia_tri):
        return (
            self.bits[self.hash1(gia_tri)] == 1
            and self.bits[self.hash2(gia_tri)] == 1
        )


bo_loc = BloomFilter()
bo_loc.add("apple")

print(f"Apple: {bo_loc.contains('apple')}")
print(f"Banana: {bo_loc.contains('banana')}")