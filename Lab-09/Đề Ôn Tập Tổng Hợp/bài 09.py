def insertion_sort(a):
    so_shift = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            so_shift += 1
            j -= 1

        a[j + 1] = key

    return so_shift


a = [3, 2, 1]
so_shift = insertion_sort(a)

print(f"Mảng sau khi sắp xếp: {a}")
print(f"Số lần dịch chuyển: {so_shift}")
