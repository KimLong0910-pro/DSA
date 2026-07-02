import math


def multiplication_hash(k, m):
    A = 0.618
    return math.floor(m * ((k * A) % 1))


print(multiplication_hash(37, 10))
