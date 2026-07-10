def binary_insertion_sort(a):
    so_shift = 0

    for i in range(1, len(a)):
        key = a[i]
        left = 0
        right = i

        while left < right:
            mid = (left + right) // 2

            if a[mid] <= key:
                left = mid + 1
            else:
                right = mid

        vi_tri = left
        j = i

        while j > vi_tri:
            a[j] = a[j - 1]
            so_shift += 1
            j -= 1

        a[vi_tri] = key

    return so_shift


a = [5, 2, 4, 6, 1]
so_shift = binary_insertion_sort(a)

print(f"Mảng sau khi sắp xếp: {a}")
print(f"Số lần dịch chuyển: {so_shift}")
