class HashSet:
    def __init__(self):
        self.data = set()

    def add(self, value):
        self.data.add(value)

    def contains(self, value):
        return value in self.data

    def remove(self, value):
        self.data.discard(value)


tap = HashSet()
tap.add(1)
tap.add(1)
tap.add(2)

print(tap.data)
