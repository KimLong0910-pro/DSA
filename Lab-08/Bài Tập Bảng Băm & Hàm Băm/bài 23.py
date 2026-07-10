def so_sanh_hash(keys, m):
    buckets = [0] * m

    for k in keys:
        vi_tri = k % m
        buckets[vi_tri] += 1

    return buckets

keys = [10, 20, 30, 40, 15]
print(so_sanh_hash(keys, 10))