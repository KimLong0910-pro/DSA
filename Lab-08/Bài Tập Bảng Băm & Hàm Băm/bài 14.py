DELETED = object()


class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def put(self, key):
        vi_tri = self.hash(key)

        while self.table[vi_tri] is not None and self.table[vi_tri] is not DELETED:
            vi_tri = (vi_tri + 1) % self.size
        self.table[vi_tri] = key

    def get(self, key):
        vi_tri = self.hash(key)

        while self.table[vi_tri] is not None:
            if self.table[vi_tri] is not DELETED and self.table[vi_tri] == key:
                return True
            vi_tri = (vi_tri + 1) % self.size

        return False

    def remove(self, key):
        vi_tri = self.hash(key)

        while self.table[vi_tri] is not None:
            if self.table[vi_tri] is not DELETED and self.table[vi_tri] == key:
                self.table[vi_tri] = DELETED
                return

            vi_tri = (vi_tri + 1) % self.size

    def hien_thi(self):
        kqua = []

        for gia_tri in self.table:
            if gia_tri is DELETED:
                kqua.append("DELETED")
            else:
                kqua.append(gia_tri)

        print(f"Bảng băm: {kqua}")


bang = HashTable()

bang.put(10)
bang.put(17)
bang.put(24)

bang.hien_thi()
bang.remove(17)
bang.hien_thi()

print(f"Tìm 24: {bang.get(24)}")
print(f"Tìm 17: {bang.get(17)}")
