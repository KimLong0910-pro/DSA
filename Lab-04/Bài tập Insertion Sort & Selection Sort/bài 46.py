def selection_compare(a):
    n = len(a)
    so_sanh = 0

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            so_sanh += 1

            if a[j] < a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]

    return so_sanh


a1 = [1, 2, 3, 4, 5]
a2 = [3, 5, 1, 4, 2]
a3 = [5, 4, 3, 2, 1]

print(selection_compare(a1.copy()))
print(selection_compare(a2.copy()))
print(selection_compare(a3.copy()))