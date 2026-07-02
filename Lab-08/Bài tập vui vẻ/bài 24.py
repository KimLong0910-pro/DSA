import random


class UniversalHash:
    def __init__(self, m):
        self.m = m
        self.p = 101
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash(self, k):
        return ((self.a * k + self.b) % self.p) % self.m


h = UniversalHash(10)
print(h.hash(37))
