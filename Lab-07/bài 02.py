class ArrayList:
    def __init__(self, suc_chua=10):
        self.data = [None] * suc_chua
        self.n = 0

    def append(self, gia_tri):
        self.data[self.n] = gia_tri
        self.n += 1

    def popBack(self):
        if self.n == 0:
            raise Exception("Empty list")
        gia_tri = self.data[self.n - 1]
        self.n -= 1
        return gia_tri


arr = ArrayList()
arr.append(1)
arr.append(2)
arr.append(3)

print(arr.popBack())
