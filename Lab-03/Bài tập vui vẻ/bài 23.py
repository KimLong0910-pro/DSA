def thong_ke(a):
    n = len(a)

    so_lan_so_sanh = 0
    swap = 0

    for i in range(n - 1):
        da_doi = False

        for j in range(n - 1 - i):
            so_lan_so_sanh += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1
                da_doi = True

        if not da_doi:
            break

    return so_lan_so_sanh, swap


a = [1, 2, 3, 4]
b = [4, 3, 2, 1]
da_xep = thong_ke(a)
xep_nguoc = thong_ke(b)
print(f"Đã sắp xếp: {da_xep}")
print(f"Sắp xếp ngược: {xep_nguoc}")
