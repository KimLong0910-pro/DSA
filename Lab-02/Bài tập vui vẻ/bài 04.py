def vi_tri_max(a, x):
    left = 0
    right = len(a) - 1
    mid = 0
    lon_nhat = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            lon_nhat = mid
            left = mid + 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return lon_nhat


a = [1, 2, 2, 2, 3]
x = 2
vi_tri = vi_tri_max(a, x)
print(f"Vị trí {x}: {vi_tri}")
