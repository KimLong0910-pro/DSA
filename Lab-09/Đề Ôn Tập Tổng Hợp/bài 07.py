def bubble_sort(a):
    n = len(a)
    so_swap = 0

    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                so_swap += 1

    return so_swap


a = [2, 3, 1]
so_swap = bubble_sort(a)

print(f"Mảng sau khi sắp xếp: {a}")
print(f"Số lần hoán đổi: {so_swap}")
