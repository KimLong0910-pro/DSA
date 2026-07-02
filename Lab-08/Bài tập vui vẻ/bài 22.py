def hash_tuple(a, b):
    c = 31
    return (hash(a) * c) ^ hash(b)


print(hash_tuple(10, 20))
