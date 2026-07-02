def hash_set(tap_hop):
    hash_value = 0

    for x in tap_hop:
        hash_value ^= hash(x)

    return hash_value

tap1 = {1, 2, 3}
tap2 = {3, 1, 2}

print(hash_set(tap1))
print(hash_set(tap2))