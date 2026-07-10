class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        vi_tri = self.hash(key)
        bucket = self.buckets[vi_tri]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        vi_tri = self.hash(key)
        bucket = self.buckets[vi_tri]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        vi_tri = self.hash(key)
        bucket = self.buckets[vi_tri]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


bang_bam = HashTable()
bang_bam.put("a", 1)
bang_bam.put("b", 2)

print(bang_bam.get("a"))
