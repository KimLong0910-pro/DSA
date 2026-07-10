class queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, gia_tri):
        if self.count == self.size:
            print("Queue đầy")
            return

        self.queue[self.rear] = gia_tri
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return None

        gia_tri = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1

        return gia_tri


queue = queue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(f"Lấy ra: {queue.dequeue()}")

queue.enqueue(40)
queue.enqueue(50)

print(f"Hàng đợi: {queue.queue}")