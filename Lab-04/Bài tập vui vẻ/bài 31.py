def selection_sort(a):
    n = len(a)
    so_sanh = 0

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            so_sanh += 1

            if a[j] < a[min_idx]:
                min_idx = j

    return so_sanh


a = [5, 2, 4, 6, 1]
kqua = selection_sort(a)

print(kqua)