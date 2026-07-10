import random


class UniversalHash:
    def __init__(self, m):
        self.m = m
        self.p = 101

        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash(self, khoa):
        return ((self.a * khoa + self.b) % self.p) % self.m


bang_bam = UniversalHash(10)
khoa = 37

print(f"a = {bang_bam.a}")
print(f"b = {bang_bam.b}")
print(f"Hash({khoa}) = {bang_bam.hash(khoa)}")
