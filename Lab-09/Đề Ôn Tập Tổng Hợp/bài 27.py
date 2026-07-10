class my_queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, gia_tri):
        self.in_stack.append(gia_tri)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()


queue = my_queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(f"Lấy ra: {queue.dequeue()}")

queue.enqueue(4)

print(f"Lấy ra: {queue.dequeue()}")