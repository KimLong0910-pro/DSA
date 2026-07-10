def dau_tien(a, x):
    left = 0
    right = len(a) - 1
    mid = 0
    dau = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            dau = mid
            right = mid - 1
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return dau


def cuoi_cung(a, x):
    left = 0
    right = len(a) - 1
    mid = 0
    cuoi = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            cuoi = mid
            left = mid + 1
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return cuoi


def dem(a, x):
    vi_tri_dau = dau_tien(a, x)
    vi_tri_cuoi = cuoi_cung(a, x)

    if vi_tri_dau == -1:
        return 0
    else:
        return vi_tri_cuoi - vi_tri_dau + 1


a = [1, 2, 2, 2, 3]
x = 2
vi_tri = dem(a, x)
print(f"Số lần xuất hiện của {x}: {vi_tri}")
