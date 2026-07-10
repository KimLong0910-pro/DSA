class HashTableLinear:
    def __init__(self, size=10):
        self.size = size
        self.bang = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        vi_tri = self.hash(key)

        while self.bang[vi_tri] is not None and self.bang[vi_tri][0] != key:
            vi_tri = (vi_tri + 1) % self.size

        self.bang[vi_tri] = (key, value)

    def get(self, key):
        vi_tri = self.hash(key)
        bdau = vi_tri

        while self.bang[vi_tri] is not None:
            if self.bang[vi_tri][0] == key:
                return self.bang[vi_tri][1]

            vi_tri = (vi_tri + 1) % self.size
            if vi_tri == bdau:
                break

        return None
    
bang_bam = HashTableLinear()
bang_bam.put("a", 1)
bang_bam.put("b", 2)

print(bang_bam.get("b"))