class ArrayList:
    def __init__(self, suc_chua=10):
        self.data = [None] * suc_chua
        self.suc_chua = suc_chua
        self.n = 0

    def add(self, gia_tri):
        if self.n == self.suc_chua:
            raise Exception("Array is full")
        self.data[self.n] = gia_tri
        self.n += 1

    def get(self, vi_tri):
        if vi_tri < 0 or vi_tri >= self.n:
            raise IndexError("Invalid index")
        return self.data[vi_tri]

    def set(self, vi_tri, gia_tri):
        if vi_tri < 0 or vi_tri >= self.n:
            raise IndexError("Invalid index")
        self.data[vi_tri] = gia_tri

    def size(self):
        return self.n


arr = ArrayList()
arr.add(1)
arr.add(2)
arr.add(3)

print(arr.get(1))
print(arr.size())
