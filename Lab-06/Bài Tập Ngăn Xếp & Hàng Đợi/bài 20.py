class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def front(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def rear(self):
        if len(self.queue) == 0:
            return None
        return self.queue[-1]


q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

print(f"front = {q.front()}")
print(f"rear = {q.rear()}")