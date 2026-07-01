class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)
        self.queue.sort()

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)


pq = PriorityQueue()
pq.enqueue(5)
pq.enqueue(2)
pq.enqueue(8)
pq.enqueue(1)

print(pq.dequeue())
print(pq.queue)