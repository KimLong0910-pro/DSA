class Deque:
    def __init__(self):
        self.deque = []

    def pushFront(self, x):
        self.deque.insert(0, x)

    def pushBack(self, x):
        self.deque.append(x)

    def popFront(self):
        if len(self.deque) == 0:
            return None
        return self.deque.pop(0)

    def popBack(self):
        if len(self.deque) == 0:
            return None
        return self.deque.pop()


d = Deque()
d.pushFront(1)
d.pushBack(2)

print(d.deque)