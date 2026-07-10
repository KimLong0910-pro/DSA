class ArrayList:
    def __init__(self, suc_chua=10):
        self.data = [None] * suc_chua
        self.n = 0

    def insert(self, vi_tri, gia_tri):
        for i in range(self.n, vi_tri, -1):
            self.data[i] = self.data[i - 1]

        self.data[vi_tri] = gia_tri
        self.n += 1

    def remove(self, vi_tri):
        removed = self.data[vi_tri]

        for i in range(vi_tri, self.n - 1):
            self.data[i] = self.data[i + 1]

        self.n -= 1
        return removed


arr = ArrayList()
arr.data[0] = 1
arr.data[1] = 2
arr.data[2] = 4
arr.n = 3

arr.insert(2, 3)

print(arr.data[: arr.n])
