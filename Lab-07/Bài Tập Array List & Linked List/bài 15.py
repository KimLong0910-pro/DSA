class ArrayList:
    def __init__(self):
        self.data = []
        self.modCount = 0

    def add(self, gia_tri):
        self.data.append(gia_tri)
        self.modCount += 1

    def __iter__(self):
        return ArrayListIterator(self)


class ArrayListIterator:
    def __init__(self, arr):
        self.arr = arr
        self.index = 0
        self.expectedModCount = arr.modCount

    def __iter__(self):
        return self

    def __next__(self):
        if self.expectedModCount != self.arr.modCount:
            raise RuntimeError("phát hiện thay đổi cấu trúc")

        if self.index >= len(self.arr.data):
            raise StopIteration

        gia_tri = self.arr.data[self.index]
        self.index += 1
        return gia_tri


arr = ArrayList()
arr.add(1)
arr.add(2)
arr.add(3)

for x in arr:
    print(x)
    arr.add(10)
