class ArrayList:
    def __init__(self, suc_chua=4):
        self.suc_chua = suc_chua
        self.data = [None] * suc_chua
        self.n = 0

    def resize(self):
        self.suc_chua *= 2
        new_data = [None] * self.suc_chua

        for i in range(self.n):
            new_data[i] = self.data[i]

        self.data = new_data

    def append(self, gia_tri):
        if self.n == self.suc_chua:
            self.resize()

        self.data[self.n] = gia_tri
        self.n += 1


arr = ArrayList(4)

for i in range(5):
    arr.append(i)
print(arr.suc_chua)
