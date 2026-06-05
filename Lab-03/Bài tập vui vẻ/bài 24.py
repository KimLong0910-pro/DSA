def so_luot_toi_thieu(ban_dau, muc_tieu):
    a = ban_dau[:]
    n = len(a)

    for i in range(n):

        if a == muc_tieu:
            return i

        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return -1


ban_dau = [4, 3, 2, 1]
muc_tieu = [3, 2, 1, 4]
kqua = so_luot_toi_thieu(ban_dau, muc_tieu)
print(kqua)