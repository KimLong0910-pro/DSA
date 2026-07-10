class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, gia_tri):
        self.stack.append(gia_tri)

        if not self.min_stack or gia_tri <= self.min_stack[-1]:
            self.min_stack.append(gia_tri)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        return self.stack.pop()

    def getMin(self):
        return self.min_stack[-1]


stack = MinStack()
stack.push(5)
stack.push(3)
stack.push(7)

print(f"Giá trị nhỏ nhất: {stack.getMin()}")