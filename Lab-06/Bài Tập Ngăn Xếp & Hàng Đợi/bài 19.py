class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.size

    def enqueue(self, x):
        if self.isFull():
            print("Queue full")
            return

        self.queue.append(x)

    def dequeue(self):
        if self.isEmpty():
            print("Queue empty")
            return None

        return self.queue.pop(0)

    def count(self):
        return len(self.queue)


q = Queue(3)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.count())
print(q.dequeue())