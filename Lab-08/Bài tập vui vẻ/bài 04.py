def tim_phan_tu_chung(arr1, arr2):
    tap_hop = set(arr1)
    kqua = set()

    for x in arr2:
        if x in tap_hop:
            kqua.add(x)

    return kqua


arr1 = [1, 2, 3]
arr2 = [2, 3, 4]

print(tim_phan_tu_chung(arr1, arr2))
