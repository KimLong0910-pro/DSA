def k_nho_nhat(ma_tran, k):
    ds = []

    for hang in ma_tran:
        ds.extend(hang)

    ds.sort()

    return ds[k - 1]


ma_tran = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]

k = 8
phan_tu = k_nho_nhat(ma_tran, k)
print(f"Phần tử nhỏ thứ {k}: {phan_tu}")



