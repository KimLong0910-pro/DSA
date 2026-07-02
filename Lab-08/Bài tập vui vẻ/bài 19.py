def dem_va_cham(keys, m):
    buckets = {}

    for key in keys:
        vi_tri = key % m

        if vi_tri not in buckets:
            buckets[vi_tri] = 0

        buckets[vi_tri] += 1

    cham = 0

    for dem in buckets.values():
        if dem > 1:
            cham += dem - 1

    return cham

keys = [10, 20, 30, 15]
print(dem_va_cham(keys, 10))