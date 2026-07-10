def shell_sort(a):
    n = len(a)
    gap = n // 2
    so_shift = 0

    while gap > 0:
        for i in range(gap, n):
            key = a[i]
            j = i

            while j >= gap and a[j - gap] > key:
                a[j] = a[j - gap]
                so_shift += 1
                j -= gap

            a[j] = key
        gap //= 2

    return so_shift


a = [9, 8, 3, 7, 5, 6, 4, 1]
so_shift = shell_sort(a)

print(f"Mảng sau khi sắp xếp: {a}")
print(f"Số lần dịch chuyển: {so_shift}")