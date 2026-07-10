def bubble_sort(a):
    n = len(a)
    so_luot = 0

    for i in range(n - 1):
        da_swap = False
        so_luot += 1

        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                da_swap = True

        if not da_swap:
            break

    return so_luot


a = [1, 2, 3, 4]
so_luot = bubble_sort(a)

print(f"Mảng sau khi sắp xếp: {a}")
print(f"Số lượt thực hiện: {so_luot}")