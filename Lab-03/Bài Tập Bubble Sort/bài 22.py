def early_exit(a):
    n = len(a)
    so_luot = 0
    so_swap = 0

    for i in range(n - 1):
        da_doi_cho = False

        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

                da_doi_cho = True
                so_swap += 1

        if da_doi_cho:
            so_luot += 1
        else:
            break

    return a, so_luot, so_swap


a = [1, 3, 2, 4, 6, 5]
mang, luot, swap = early_exit(a)
print(f"Mảng sau khi sắp xếp: {mang}")
print(f"Số lượt: {luot}")
print(f"Số swap: {swap}")