class hitCounter:
    def __init__(self):
        self.queue = []

    def hit(self, time):
        self.queue.append(time)

    def get_hits(self, time):
        while self.queue and self.queue[0] <= time - 300:
            self.queue.pop(0)

        return len(self.queue)


counter = hitCounter()

counter.hit(1)
counter.hit(2)
counter.hit(300)

print(counter.get_hits(300))
print(counter.get_hits(301))