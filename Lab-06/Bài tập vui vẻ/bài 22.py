class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def reverse(self):
        stack = []

        while self.queue:
            stack.append(self.queue.pop(0))

        while stack:
            self.queue.append(stack.pop())


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.reverse()
print(q.queue)