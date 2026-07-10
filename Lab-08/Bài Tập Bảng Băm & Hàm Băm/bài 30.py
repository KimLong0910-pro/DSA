def minhash(tap_hop):
    return min(hash(x) for x in tap_hop)


def jaccard(tap1, tap2):
    return minhash(tap1) == minhash(tap2)


tap1 = {1, 2, 3}
tap2 = {2, 3, 4}

print(jaccard(tap1, tap2))
