def chan_dau_tien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i


a = [3, 7, 11, 8, 5, 4]
kqua = chan_dau_tien(a)
print(f"Vị trí: {kqua}")
