def hash_2d(ma_tran):
    hash_value = 0
    p = 31
    mod = 10**9 + 7

    for hang in ma_tran:
        for x in hang:
            hash_value = (hash_value * p + x) % mod

    return hash_value


ma_tran = [[1, 2], [3, 4]]

print(hash_2d(ma_tran))
