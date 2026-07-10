def vi_tri_dau(a, x):
    left = 0
    right = len(a) - 1
    kqua = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            kqua = mid
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return kqua


def vi_tri_cuoi(a, x):
    left = 0
    right = len(a) - 1
    kqua = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            kqua = mid
            left = mid + 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return kqua


a = [1, 2, 2, 2, 3]
x = 2
dau = vi_tri_dau(a, x)
cuoi = vi_tri_cuoi(a, x)

if dau == -1:
    dem = 0
else:
    dem = cuoi - dau + 1

print(f"Vị trí đầu: {dau}")
print(f"Vị trí cuối: {cuoi}")
print(f"Số lần xuất hiện: {dem}")
