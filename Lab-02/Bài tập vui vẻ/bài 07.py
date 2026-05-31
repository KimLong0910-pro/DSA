def upper_bound(a, x):
    left = 0
    right = len(a) - 1
    kqua = len(a)

    while left <= right:
        mid = (left + right) // 2

        if a[mid] > x:
            kqua = mid
            right = mid - 1
        else:
            left = mid + 1

    return kqua


a = [1, 3, 5, 7]
x = 5
vi_tri = upper_bound(a, x)
print(f"Vị trí của {x}: {vi_tri}")
