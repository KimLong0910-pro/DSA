class BloomFilter:
    def __init__(self, size=10):
        self.size = size
        self.bits = [0] * size

    def hash1(self, x):
        return hash(x) % self.size

    def hash2(self, x):
        return (hash(x) * 7) % self.size

    def add(self, x):
        self.bits[self.hash1(x)] = 1
        self.bits[self.hash2(x)] = 1

    def contains(self, x):
        return self.bits[self.hash1(x)] == 1 and self.bits[self.hash2(x)] == 1


bf = BloomFilter()
bf.add("apple")

print(bf.contains("apple"))
print(bf.contains("banana"))
