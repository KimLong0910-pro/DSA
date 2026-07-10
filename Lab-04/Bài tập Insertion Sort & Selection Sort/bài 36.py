def selection_sort(a):
    n = len(a)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]

    return a


a = [(2, "a"), (2, "b"), (1, "c")]

print(f"Ban đầu: {a}")
print(f"Sau sort: {selection_sort(a)}")
