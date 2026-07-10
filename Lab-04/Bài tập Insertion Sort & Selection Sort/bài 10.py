def insertion_sort_shift(a):
    n = len(a)
    so_lan_hoan_doi = 0

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            so_lan_hoan_doi += 1
            j -= 1

        a[j + 1] = key

    return so_lan_hoan_doi


def dem_nghich_the(a):
    dem = 0
    n = len(a)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                dem += 1

    return dem


a = [2, 4, 1, 3]

mang_sap_xep = a.copy()
so_nghich_the = dem_nghich_the(a)
so_shift = insertion_sort_shift(mang_sap_xep)

print(f"Mảng ban đầu: {a}")
print(f"Mảng sau khi sắp xếp: {mang_sap_xep}")
print(f"Số nghịch thế: {so_nghich_the}")
print(f"Số shift: {so_shift}")
